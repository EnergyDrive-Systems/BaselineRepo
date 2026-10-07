(() => {
  "use strict";
  const slides = Array.from(document.querySelectorAll(".slide"));
  const picker = document.querySelector("#slide-picker");
  const previous = document.querySelector("#previous");
  const next = document.querySelector("#next");
  const fullscreen = document.querySelector("#fullscreen");
  const announcement = document.querySelector("#announcement");

  function showSlide(index, updateHash = true) {
    const selected = Math.max(0, Math.min(slides.length - 1, index));
    slides.forEach((slide, position) => {
      slide.hidden = position !== selected;
    });
    picker.value = String(selected);
    previous.disabled = selected === 0;
    next.disabled = selected === slides.length - 1;
    announcement.textContent = `Slide ${selected + 1} of ${slides.length}: ${slides[selected].dataset.title}`;
    document.title = `${slides[selected].dataset.title} | ${document.body.dataset.deckTitle || "EnergyDrive Development Baseline"}`;
    if (updateHash) history.replaceState(null, "", `#slide-${selected + 1}`);
    window.scrollTo({ top: 0, behavior: "instant" });
  }

  function showHash() {
    const match = /^#slide-(\d+)$/.exec(location.hash);
    const number = match ? Number(match[1]) : 0;
    showSlide(number >= 1 && number <= slides.length ? number - 1 : 0, false);
  }

  previous.addEventListener("click", () => showSlide(Number(picker.value) - 1));
  next.addEventListener("click", () => showSlide(Number(picker.value) + 1));
  picker.addEventListener("change", () => showSlide(Number(picker.value)));
  window.addEventListener("hashchange", showHash);
  document.querySelector("#print").addEventListener("click", () => window.print());
  fullscreen.addEventListener("click", async () => {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await document.documentElement.requestFullscreen();
    } catch {
      announcement.textContent = "Fullscreen is unavailable in this browser.";
    }
  });
  document.addEventListener("fullscreenchange", () => {
    const active = Boolean(document.fullscreenElement);
    const label = active ? "Exit fullscreen" : "Enter fullscreen";
    fullscreen.title = label;
    fullscreen.setAttribute("aria-label", label);
  });
  document.addEventListener("keydown", (event) => {
    if (event.altKey || event.ctrlKey || event.metaKey || /INPUT|SELECT|TEXTAREA|BUTTON/.test(event.target.tagName)) return;
    const actions = {
      ArrowRight: () => showSlide(Number(picker.value) + 1),
      PageDown: () => showSlide(Number(picker.value) + 1),
      ArrowLeft: () => showSlide(Number(picker.value) - 1),
      PageUp: () => showSlide(Number(picker.value) - 1),
      Home: () => showSlide(0),
      End: () => showSlide(slides.length - 1),
    };
    if (actions[event.key]) {
      event.preventDefault();
      actions[event.key]();
    }
  });

  if (window.lucide) {
    window.lucide.createIcons();
    document.body.classList.add("icons-ready");
  }
  if (!document.documentElement.requestFullscreen) fullscreen.hidden = true;
  showHash();
})();