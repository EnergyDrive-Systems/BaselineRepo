# Baseline Infographic Deck

Five-slide, 16:9 EnergyDrive presentation for technical and business stakeholders:

1. Shared foundation and purpose.
2. Container/venv developer startup.
3. Standards, Material 3, and ten agent skills.
4. Python, Ignition, database, and Terraform coverage.
5. Controlled delivery and project activation requirements.

## Present Or Share

Open [baseline.html](baseline.html) in a browser, or share [baseline.pdf](baseline.pdf).
No development server, cloud connection, or dependency installation is required to view
the deck. Keep its folder together with the repository's `assets/brand/` folder when
sharing the HTML; the PDF is standalone. The deck is not a native PowerPoint file.

Use the slide selector or navigation buttons. Arrow/Page keys navigate when focus is
outside the controls; Home/End select the first/last slide. Fullscreen is browser-dependent.
The print button prints all five slides, not just the visible one. To regenerate the PDF,
choose Save as PDF, retain the 16:9 page sizing, enable background graphics, and disable
browser headers/footers. Confirm all five pages after export.

Edit `baseline.html` for content, `baseline.css` for tokens/layout/print styling, and
`baseline.js` for controls. Re-export the PDF after changing presentation content or print
styles. The small original logo is unmodified; do not upscale it into a print master.
System-installed Bahnschrift/Trebuchet fonts have fallbacks; appearance can vary by OS.

## Sources And Accuracy

Content summarizes the shared standards, profiles, skills, and deployment guidance.
Update the slides when those sources change. The baseline supplies scaffolding, not a
deployed application. Real adapters, protections, owners, and runtime acceptance remain
project responsibilities. Instructions are not deterministic enforcement, and agents
receive no production execution authority.

## Third-Party Asset

Lucide 0.468.0 is vendored locally for offline icons. Preserve `lucide.LICENSE` with it;
this dependency's original notice/license was downloaded unchanged.

- Source: https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js
- License: https://unpkg.com/lucide@0.468.0/LICENSE
- SHA256: `3411692820CB8D47543F69496AA25FD603A358F4498046F41C508A5A3342210E`

Do not auto-update the library or fonts at presentation time.