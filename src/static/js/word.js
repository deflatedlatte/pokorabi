document.getElementById("word-user-submit-btn").addEventListener("click", async (e) => {
  const userInput = document.getElementById("word-user-input").value;

  const queryParams = new URLSearchParams();
  queryParams.set("word", userInput);
  const result = await fetch(`/api/sentences?${queryParams}`).then(r => r.json());

  document.getElementById("word-user-asked").textContent = userInput;
  const list = document.getElementById("example-list");
  list.textContent = "";
  for (const sentence of result) {
    const entry = document.createElement("li");
    entry.textContent = sentence;
    list.appendChild(entry);
  }
});
