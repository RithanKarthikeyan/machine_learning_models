console.log("Spam detector extension loaded");

let lastEmailText = "";

function extractEmailText() {
  // Gmail email body selector (stable)
  const emailBody = document.querySelector("div.a3s");
  if (!emailBody) return null;
  return emailBody.innerText.trim();
}

function checkSpam(emailText) {
  fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: emailText })
  })
    .then(res => res.json())
    .then(data => {
      showBanner(
        data.prediction === "spam"
          ? "🚨 This email is predicted as SPAM"
          : "✅ This email looks SAFE",
        data.prediction === "spam"
      );
    })
    .catch(err => {
      console.error("Spam API error:", err);
    });
}

function showBanner(text, isSpam) {
  if (document.getElementById("spam-banner")) return;

  const banner = document.createElement("div");
  banner.id = "spam-banner";
  banner.innerText = text;
  banner.style.position = "fixed";
  banner.style.top = "0";
  banner.style.left = "0";
  banner.style.width = "100%";
  banner.style.padding = "10px";
  banner.style.zIndex = "9999";
  banner.style.fontSize = "16px";
  banner.style.fontWeight = "bold";
  banner.style.textAlign = "center";
  banner.style.color = "white";
  banner.style.backgroundColor = isSpam ? "#d93025" : "#1e8e3e";

  document.body.appendChild(banner);
}

const observer = new MutationObserver(() => {
  const emailText = extractEmailText();
  if (!emailText || emailText === lastEmailText) return;

  lastEmailText = emailText;
  console.log("Checking email for spam...");
  checkSpam(emailText);
});

observer.observe(document.body, {
  childList: true,
  subtree: true
});
