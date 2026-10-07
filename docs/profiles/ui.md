# UI Design Profile

## Mandatory Default

Use **Material Design 3 (Material 3 / M3)** principles for all new and changed user
interfaces, including web, mobile, desktop, and Ignition Perspective. Agents load this
profile automatically before UI work; users do not need to request Material 3 each time.
Do not substitute another design system without explicit owner approval and a documented
exception under the shared standards. Do not redesign unrelated legacy screens in a
small change; apply the standard to the affected flow and record any migration gaps.

Material 3 is an adaptable design system, not a guarantee of usability or accessibility.
Choose components and density for real user tasks and validate the resulting experience.
This profile complements, rather than replaces, runtime, branding, and SCADA rules.

## Foundations And Components

- Define shared design tokens for semantic color roles, typography, spacing, shape,
  elevation, and motion. Use primary/secondary/tertiary, surface/on-surface, outline,
  and error roles instead of scattering literal styling values across screens.
- Apply EnergyDrive branding through approved theme tokens and the original assets
  described in `assets/brand/README.md`. Brand colors must not obscure alarm semantics
  or produce low-contrast text. Do not recolor the supplied logo or invent brand variants.
- Use Material 3 typography roles for display, headline, title, body, and labels;
  match hierarchy to information density, not viewport width. Keep fonts readable and
  support user text scaling. Use spacing, grouping, and restrained elevation deliberately.
- Choose familiar components for each interaction: buttons for commands, switches or
  checkboxes for binary values, menus/selects for choices, and suitable numeric controls.
  Use consistent icons with accessible names and tooltips for unfamiliar icon controls.
- Provide default, hover, focus, pressed, selected, disabled, and validation states where
  applicable. Include loading, empty, error, success, offline/stale, and recovery behavior
  for data-driven screens. Never present stale equipment data as an unqualified healthy state.
- Keep navigation predictable, preserve meaningful user context, and make primary tasks
  direct. Tables and dashboards support scanning, filtering, comparison, and repeated
  actions; do not turn operational interfaces into decorative marketing layouts.
- Use responsive layouts and adaptive navigation for compact, medium, and expanded
  windows. Avoid overlapping/clipped labels and unstable controls. Respect reduced-motion
  preferences and use animation only when it communicates state or continuity.

## Accessibility And Human Factors

Target WCAG 2.2 AA for browser-based interfaces, with platform-equivalent accessibility
checks for other UIs. Validate keyboard operation, visible/unobscured focus, meaningful
labels, assistive-technology semantics, and logical reading/focus order. Do not convey
status only through color, and do not rely on placeholders as field labels.

Check applicable contrast thresholds: at least 4.5:1 for normal text, 3:1 for qualifying
large text, and 3:1 for required non-text control/graphic contrast, observing WCAG's
defined exceptions. Aim for 48 x 48 logical-pixel touch targets; verify platform units
and actual hit areas rather than blindly equating hardware pixels with CSS pixels/dp.
Compact controls still need accessible target sizing/spacing and keyboard alternatives.

Give errors actionable text, preserve entered data when practical, and communicate
pending versus completed actions accurately. Critical equipment controls need clear
identity, current context, and the existing confirmation/interlock rules. Alarm visibility,
site-specific safety conventions, and operator readability take precedence over decorative
Material effects. Any conflicting adaptation needs a documented, reviewed resolution.

## Platform Implementation

Use a maintained framework-compatible Material 3 implementation where appropriate;
verify its actual M3 support, accessibility, and version rather than assuming any library
named Material supplies it. Reuse existing approved components and pin dependencies.
Do not add a frontend framework or component library to a project that does not need it.

For Ignition Perspective, map the principles to native components, shared style classes,
reusable views, and supported theme/CSS tokens. Ignition is not automatically an M3
component library. Do not embed a separate web application merely for visual conformity
or rely on fragile generated-DOM selectors. Document platform limitations and test in
the actual gateway/browser, not solely in a standalone mockup.

## Acceptance Evidence

Before completing a UI change, record the chosen tokens/components and test the affected
flow on representative desktop and mobile/tablet sizes, plus the actual operator display
or touch panel when applicable. Check long labels, zoom/text scaling, navigation, keyboard
focus, touch targets, contrast, and loading/empty/error/stale states. Capture screenshots
and interaction results; run automated accessibility checks where supported and supplement
them with manual review. Screenshots alone do not prove accessibility or usability.

The standards review checks this profile; the requirements review checks that the intended
user tasks work. Include evidence and limitations in the PR and change record. Missing
runtime checks remain unverified. Agent routing and checklists guide compliance; this
policy does not itself implement an application UI or supply a CI test that certifies
Material 3 conformance. Presentation examples are not proof of project UI acceptance.

## References

- Material 3 foundations: https://m3.material.io/foundations
- Material 3 components: https://m3.material.io/components
- WCAG 2.2: https://www.w3.org/TR/WCAG22/