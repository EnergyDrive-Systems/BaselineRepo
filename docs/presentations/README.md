# Baseline Infographic Deck

Five-slide, 16:9 EnergyDrive presentation for technical and business stakeholders:

1. Shared foundation and purpose.
2. Container/venv developer startup.
3. Standards, Material 3, and ten agent skills.
4. Python, Ignition, database, and Terraform coverage.
5. Controlled delivery and project activation requirements.

## Detailed First-Project Walkthrough

Separate from the five-slide overview, [first-project.html](first-project.html) and
[first-project.pdf](first-project.pdf) provide a 17-slide infographic version of
[Your First Project](../getting-started.md), rewritten for inexperienced project users.
It starts with plain-English terms, then GitHub template buttons, VS Code's clone dialog,
container reopening, menu-driven checks, Testing, agent chat, GUI branches/commits/PRs,
returning to work, and beginner troubleshooting. Owner/helper duties are the final optional
appendix, not the main user's starting point.

The written guide remains the source of truth. Keep menu names/checkpoints and both chat
prompts synchronized when editing it or the deck. The slides contain no terminal blocks;
their two copyable boxes are plain-language agent prompts (formatting indentation may vary).
Optional technical commands remain in the written guide's helper appendix. No command-line
knowledge or template-administration role is assumed for the beginner flow.

## Present Or Share

Open [baseline.html](baseline.html) in a browser, or share [baseline.pdf](baseline.pdf).
No development server, cloud connection, or dependency installation is required to view
the deck. Keep its folder together with the repository's `assets/brand/` folder when
sharing the HTML; the PDF is standalone. The deck is not a native PowerPoint file.

Use the slide selector or navigation buttons. Arrow/Page keys navigate when focus is
outside the controls; Home/End select the first/last slide. Fullscreen is browser-dependent.
The print button prints every slide of the open deck, not just the visible one.
To regenerate a PDF,
choose Save as PDF, retain the 16:9 page sizing, enable background graphics, and disable
browser headers/footers. Confirm five pages for the overview or 17 for the user walkthrough.

Edit `baseline.html` for content, `baseline.css` for tokens/layout/print styling, and
`baseline.js` for controls. Re-export the PDF after changing presentation content or print
styles. The small original logo is unmodified; do not upscale it into a print master.
System-installed Bahnschrift/Trebuchet fonts have fallbacks; appearance can vary by OS.

The detailed deck adds `first-project.html` and `first-project.css`, reusing the overview's
base styles, variable-slide-count navigation, local icons, and license. Preserve those
shared files and the repository's logo folder for offline HTML use. Each PDF is standalone.

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