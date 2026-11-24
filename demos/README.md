# Accessibility demos

Small interactive demos that show accessibility criteria for extended reality (XR) in action. They support the
Metaverse Standards Forum (MSF) XR Accessibility Guidelines, which are written by the Accessibility in the
Metaverse Working Group.

**Status:** this is a working proposal. The working group has not approved the demos, the list of ideas, or the
way they are organized.

## Contents

- [Why we are making demos](#why-we-are-making-demos)
- [Demos so far](#demos-so-far)
- [Ideas for more demos](#ideas-for-more-demos)
- [Poor fits for a browser demo](#poor-fits-for-a-browser-demo)
- [Open questions](#open-questions)
- [What each demo should include](#what-each-demo-should-include)
- [How to test a demo](#how-to-test-a-demo)
- [How to run a demo](#how-to-run-a-demo)
- [How to contribute](#how-to-contribute)

## Why we are making demos

- **To explain.** A criterion is easier to understand when you can try it.
- **To get better feedback.** Building a draft criterion shows whether its wording can be built and tested.
- **To compare.** Where it helps, a demo can let people switch an accessibility feature on and off.

A demo shows one possible way to meet a criterion. It is not the only way, and it is not evidence that any product
conforms to the guidelines.

The [XR Accessibility Guidelines working document][working-doc] is the source of truth. If a demo and the working
document disagree, the working document is right.

## Demos so far

### Keyboard Focus in 3D

Location: [`keyboard-focus-3d/index.html`](keyboard-focus-3d/index.html)

Move keyboard focus between five objects in a 3D scene. The 3D canvas is hidden from assistive technology, and
regular page buttons stand in for the objects.

Criteria it shows:

- **Interactive Elements (Focus):**
  - text labels;
  - a logical order to step through;
  - a view that turns to the focused object;
  - a focus indicator that points to objects out of view;
  - feedback when you have looped.
- **Content on Hover or Focus:** extra labels can be dismissed.
- **Dragging Movements:** every drag has a button alternative.
- **Speed of Interaction:** camera movement can be slowed down.

Testing so far, in one desktop browser:

| Check | Result |
| --- | --- |
| Tab, Shift+Tab, arrow keys, Home, Enter, Space and Escape | Works |
| Out-of-view notices ("to your left" and "behind you") | Works |
| Page reflow at 320 pixels wide | No horizontal scrolling |
| Dark mode | Displays correctly in one spot check |
| Full contrast measurement | Not done |
| Automated accessibility check | Not done |
| Reduced motion | Not tested |
| Zoom to 200% | Not tested |
| Screen readers | Not tested |
| Touch screens and headsets | Not tested |

Known issues:

- At 320 pixels wide, the camera buttons cover much of the scene.
- The out-of-view notice waits for the camera to stop, which can take up to 1.5 seconds.

## Ideas for more demos

The ideas are ordered by how much a demo adds over text, how well a browser can show the idea, and how many
criteria it covers. The order is a suggestion.

Criterion names come from the accepted text of the working document, as of November 20, 2026. Suggested edits that
were still waiting for a decision are not included. "Experimental" marks criteria that have a star in the working
document: needs that are essential for full access but not yet widely implemented.

### Build first

| Number | Demo | What people would try | Criteria |
| --- | --- | --- | --- |
| 1 | Spatial captions | Two speakers talk in a 3D room. Turn away, and the captions point to who is speaking. Adjust caption size, background, follow speed and position. | Captions; Caption formatting |
| 2 | Movement and comfort | Cross the same space by teleporting, moving freely or using buttons. Turn a vignette (darkened edges), snap turning and head-bob on and off. Hear a description of the destination. | Virtual Motion; Motion Sickness; Body Movement |
| 3 | Find the fountain | Reach a landmark with the screen blank, using sound beacons and spoken directions, or jump straight to it. | Points of Interest; Audio; Multimodality |
| 4 | Describe what is around me | Press a key to hear what is in view, or browse the room by area, like headings on a web page. | Audio Descriptions (on demand is experimental); Interactive Elements (experimental) |
| 5 | Notification manager | Urgent and minor alerts arrive together. Set their position and timing, and review the ones you missed. | Notifications; Multimodality |

Spatial captions is the suggested starting point. Its two sections hold about 20 criteria. Several have numbers that
can be measured, such as a minimum cap height of 0.7 degrees and lines of roughly 36 characters.

### Build next

| Number | Demo | What people would try | Criteria |
| --- | --- | --- | --- |
| 6 | Find the odd one out | Solve one puzzle by color, text label or sound. | Use of Color; Multimodality |
| 7 | Aim and select | Select small, distant targets while the demo simulates a tremor. Turn on larger targets, smoothing and highlighting. | Target Size; Target Indication; Range of Motion (motion sensitivity is experimental); Speed of Interaction |
| 8 | Your controls | Remap keys, swap holding for toggling, change sensitivity, and play with one hand. | Remappable Controls; Button Use; Control Sensitivity; Handedness |
| 9 | Head-locked or world-locked | Lean in to read a panel that follows you, then pin it in place. Change text size, contrast and brightness. | User Interface Customization; Text; Global Display Settings |
| 10 | Quiet the scene | Reduce a busy scene to what matters. Set separate volumes, switch to mono, and lower other audio while a screen reader speaks. | Avoid Sensory Overload; Audio |
| 11 | Portal and undo | Walk into a portal with and without a confirmation step. Undo a destructive action. | Major Transitions; Error Prevention |
| 12 | Take your time | Turn off, adjust or extend a time limit. Pause a cutscene and replay instructions. | Timing Adjustable; Pausing; Replayability |

### Build later

| Number | Demo | What people would try | Criteria |
| --- | --- | --- | --- |
| 13 | First-run setup | Complete or skip setup with a keyboard. If there is no input, accessibility features turn on by themselves. | Initial Customization; Menus; Accessibility Shortcuts |
| 14 | Social space | Talk with simulated people by text or pings, with speech turned into text and text turned into speech. Mute or turn down one person. | Communication; Audio |
| 15 | Any height | Reach the same shelf from standing, seated and lying-down heights. | Height; Body Position |
| 16 | Content warnings | Get a warning before a scene, then soften or skip it. | Mental Health Best Practices |

## Poor fits for a browser demo

- **Need real hardware:** hand tracking, eye tracking, sign language motion capture and most haptics (touch
  feedback).
- **Need evidence from people or policies:** Algorithms and Documentation.
- **Safety risk:** Photosensitivity. A demo could show the advance warning, but must never show flashing content.

## Open questions

These affect specific demos and are for the working group to decide.

- **Keyboard Focus in 3D:** is turning the view when focus moves a change of view, or a change of context? One
  criterion asks for the view to turn. Another says focus should not cause a major change of context.
- **Demo 4, Describe what is around me:** the Audio Descriptions tags list Hearing and Cognitive, but not Vision. Is
  that intended?
- **Demo 7, Aim and select:** Target Size gives 48 × 48 pixels or approximately 3° of the field of view. A pixel has
  no fixed size in degrees in XR, so which one should the demo use? The section also has no Requirement or Best
  Practice tag.

## What each demo should include

- A short explanation of what to do, including the keyboard controls.
- The scene, plus regular page controls that do the same things.
- A status message that screen readers announce.
- The MSF criteria it covers, then any Web Content Accessibility Guidelines (WCAG) 2.2 success criteria, with links.
- Its limitations, including what has not been tested.

Each demo is a web page, so it must itself meet WCAG 2.2 level AA. Demos should also:

- use few dependencies, with exact version numbers;
- use no tracking, and collect no personal data;
- respect the reduced motion setting;
- use original or properly licensed content, with credit.

## How to test a demo

Report what was tested and what was not.

1. Use the keyboard only. Check that focus is always visible and never trapped.
2. Use at least one screen reader, such as NVDA or VoiceOver. A person has to do this check.
3. Check light and dark modes, and measure contrast.
4. Turn on reduced motion in the system settings.
5. Zoom to 200%, and check reflow at 320 pixels wide.
6. Run an automated checker, such as axe-core. Automated checks find only some problems.
7. Ask someone to compare the demo with the criteria in the working document.

Feedback from disabled people matters most. Where possible, include people with the access needs a demo is about.

## How to run a demo

The current demo needs an internet connection, because it loads the A-Frame 3D library from a content delivery
network. With Python installed, run this from the `demos` folder:

```shell
python -m http.server 8000 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8000/keyboard-focus-3d/` in a browser.

## How to contribute

You do not need to be a programmer. Testing a demo or suggesting an idea helps.

- Email the chairs at
  [accessibility-chair@lists.metaverse-standards.org](mailto:accessibility-chair@lists.metaverse-standards.org).
- To suggest a change to a criterion, comment on the [XR Accessibility Guidelines working document][working-doc].
- To suggest a change to a demo, open a pull request. Pull requests from people who are not MSF members are reviewed
  by the Forum membership before they are accepted.

[working-doc]: https://docs.google.com/document/d/1wRHflVnJhRqZh6IvVAbWZGm0qXrkcJ2RxdRNaQjsMdY/edit?usp=sharing
