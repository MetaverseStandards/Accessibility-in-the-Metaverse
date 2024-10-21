# XR Accessibility Guidelines Collection

## 1. Notice

Copyright © 2024 James Maki. All rights reserved.

## 2. Authors

- [James Maki](https://jamesmaki.com) | [Inclusive Reality](https://inclusivereality.com) | [james.maki@inclusivereality.com](mailto:james.maki@inclusivereality.com)

## 3. Table of Contents

<!-- TOC -->

- [1. Notice](#1-notice)
- [2. Authors](#2-authors)
- [3. Table of Contents](#3-table-of-contents)
- [4. Definitions](#4-definitions)
    - [4.1. Metaverse](#41-metaverse)
    - [4.2. Accessibility](#42-accessibility)
    - [4.3. Inclusive design](#43-inclusive-design)
    - [4.4. User experience](#44-user-experience)
- [5. Accessible Product Design Requirements & Responsibilities](#5-accessible-product-design-requirements--responsibilities)
    - [5.1. Comfort](#51-comfort)
        - [5.1.1. Sensory Overload](#511-sensory-overload)
        - [5.1.2. Motion Sickness](#512-motion-sickness)
        - [5.1.3. Green Room](#513-green-room)
        - [5.1.4. Content Comfort](#514-content-comfort)
        - [5.1.5. Haptics](#515-haptics)
    - [5.2. Mobility & Body Mechanics](#52-mobility--body-mechanics)
        - [5.2.1. Settings](#521-settings)
        - [5.2.2. Height](#522-height)
        - [5.2.3. Weight](#523-weight)
        - [5.2.4. Body Position](#524-body-position)
        - [5.2.5. Handedness](#525-handedness)
        - [5.2.6. Single Handed](#526-single-handed)
        - [5.2.7. Buttons Use](#527-buttons-use)
        - [5.2.8. Locomotion](#528-locomotion)
        - [5.2.9. Object Pickup](#529-object-pickup)
        - [5.2.10. Menu Access](#5210-menu-access)
        - [5.2.11. Controls](#5211-controls)
        - [5.2.12. Dexterity](#5212-dexterity)
        - [5.2.13. Hand Tracking](#5213-hand-tracking)
        - [5.2.14. Eye Tracking](#5214-eye-tracking)
        - [5.2.15. Body Tracking](#5215-body-tracking)
        - [5.2.16. Neural Interfaces](#5216-neural-interfaces)
        - [5.2.17. Dynamic Foveated Rendering](#5217-dynamic-foveated-rendering)
    - [5.3. Cognitive](#53-cognitive)
        - [5.3.1. Difficulty](#531-difficulty)
        - [5.3.2. Complexity](#532-complexity)
        - [5.3.3. Memory](#533-memory)
        - [5.3.4. Assistance](#534-assistance)
        - [5.3.5. World Exploration](#535-world-exploration)
        - [5.3.6. Speed](#536-speed)
    - [5.4. Context](#54-context)
        - [5.4.1. Classroom support](#541-classroom-support)
        - [5.4.2. Moderation](#542-moderation)
        - [5.4.3. General (Saving Settings)](#543-general-saving-settings)
        - [5.4.4. Space Constraints](#544-space-constraints)
    - [5.5. Language & Communication](#55-language--communication)
        - [5.5.1. Reading Comprehension](#551-reading-comprehension)
        - [5.5.2. Hearing](#552-hearing)
        - [5.5.3. Subtitles / Closed Captions](#553-subtitles--closed-captions)
        - [5.5.4. Sign Language](#554-sign-language)
        - [5.5.5. Language Localization](#555-language-localization)
        - [5.5.6. Language Input](#556-language-input)
        - [5.5.7. General Accessibility Options Easy to Find](#557-general-accessibility-options-easy-to-find)
    - [5.6. Sensory](#56-sensory)
        - [5.6.1. Visual](#561-visual)
        - [5.6.2. Color Blindness](#562-color-blindness)
        - [5.6.3. Scrims and Overlays](#563-scrims-and-overlays)
        - [5.6.4. Audio](#564-audio)
        - [5.6.5. Sensory Feedback](#565-sensory-feedback)
        - [5.6.6. User Interface (UI)](#566-user-interface-ui)
        - [5.6.7. User Interface (UI) Navigation](#567-user-interface-ui-navigation)
        - [5.6.8. User Interface (UI) Focus Handling](#568-user-interface-ui-focus-handling)
        - [5.6.9. User Interface (UI) Context](#569-user-interface-ui-context)
        - [5.6.10. User Interface (UI) Horizontal](#5610-user-interface-ui-horizontal)
        - [5.6.11. User Interface (UI) Vertical](#5611-user-interface-ui-vertical)
        - [5.6.12. User Interface (UI) Direct touch interactions](#5612-user-interface-ui-direct-touch-interactions)
        - [5.6.13. Content Oriented](#5613-content-oriented)
        - [5.6.14. Digital Object Behavior](#5614-digital-object-behavior)
        - [5.6.15. Responsiveness](#5615-responsiveness)
    - [5.7. Visual & Motion Design](#57-visual--motion-design)
        - [5.7.1. Animations](#571-animations)
        - [5.7.2. Transitions](#572-transitions)
        - [5.7.3. Orientation & Layout](#573-orientation--layout)
        - [5.7.4. Depth](#574-depth)
            - [5.7.4.1. Creating Depth Using 2.5D](#5741-creating-depth-using-25d)
            - [5.7.4.2. Creating Depth Using 3D](#5742-creating-depth-using-3d)
            - [5.7.4.3. Depth as a Visual Hint](#5743-depth-as-a-visual-hint)
        - [5.7.5. Shape and Form](#575-shape-and-form)
        - [5.7.6. Texture](#576-texture)
        - [5.7.7. Colors](#577-colors)
        - [5.7.8. Typography](#578-typography)
        - [5.7.9. Iconography](#579-iconography)
        - [5.7.10. Motion Design](#5710-motion-design)
            - [5.7.10.1. Transitions](#57101-transitions)
            - [5.7.10.2. Transitions as Visual Hints](#57102-transitions-as-visual-hints)
            - [5.7.10.3. Guidance Animations](#57103-guidance-animations)
            - [5.7.10.4. Ambient Animations](#57104-ambient-animations)
    - [5.8. Playtesting](#58-playtesting)
        - [5.8.1. Range of Abilities / Play Styles](#581-range-of-abilities--play-styles)
        - [5.8.2. Diverse Playtesters](#582-diverse-playtesters)
    - [5.9. Inclusivity](#59-inclusivity)
        - [5.9.1. Inclusive representation](#591-inclusive-representation)
    - [5.10. Text display](#510-text-display)
        - [5.10.1. Text size](#5101-text-size)
        - [5.10.2. Icon and glyph sizes](#5102-icon-and-glyph-sizes)
        - [5.10.3. Text scaling](#5103-text-scaling)
        - [5.10.4. Typefaces and Font styling](#5104-typefaces-and-font-styling)
        - [5.10.5. Text Spacing](#5105-text-spacing)
        - [5.10.6. Text Case and Alignment](#5106-text-case-and-alignment)
    - [5.11. Contrast](#511-contrast)
        - [5.11.1. Contrast Ratio Chart](#5111-contrast-ratio-chart)
    - [5.12. Visual and Audio Cues](#512-visual-and-audio-cues)
    - [5.13. Screen Narration](#513-screen-narration)
    - [5.14. Input](#514-input)
        - [5.14.1. General Input](#5141-general-input)
        - [5.14.2. Mobile Input](#5142-mobile-input)
        - [5.14.3. Virtual Inputs](#5143-virtual-inputs)
        - [5.14.4. Voice Recognition Input](#5144-voice-recognition-input)
        - [5.14.5. Gaze Control Input](#5145-gaze-control-input)
    - [5.15. Difficulty Options](#515-difficulty-options)
    - [5.16. Objective Clarity](#516-objective-clarity)
    - [5.17. Audio Description](#517-audio-description)
    - [5.18. Error Messages and Destructive Actions](#518-error-messages-and-destructive-actions)
    - [5.19. Time Limits](#519-time-limits)
    - [5.20. Visual Distractions and Motion Settings](#520-visual-distractions-and-motion-settings)
    - [5.21. Photosensitivity](#521-photosensitivity)
        - [5.21.1. Luminance flash failure](#5211-luminance-flash-failure)
        - [5.21.2. Red flash failure](#5212-red-flash-failure)
        - [5.21.3. Spatial pattern failure](#5213-spatial-pattern-failure)
    - [5.22. Speech-to-Text (STS) & Text-to-Speech (TTS) Chat](#522-speech-to-text-sts--text-to-speech-tts-chat)
    - [5.23. Communication Experiences](#523-communication-experiences)
        - [5.23.1. Navigating to communication features](#5231-navigating-to-communication-features)
        - [5.23.2. Configuring the Communication Experience](#5232-configuring-the-communication-experience)
        - [5.23.3. Using Communication Features](#5233-using-communication-features)
    - [5.24. Accessible Feature Documentation](#524-accessible-feature-documentation)
    - [5.25. Accessible Customer Support](#525-accessible-customer-support)
    - [5.26. Mental Health Best Practices](#526-mental-health-best-practices)
    - [5.27. Multiuser](#527-multiuser)
    - [5.28. Physical Objects](#528-physical-objects)
    - [5.29. Product Marketing Requirements](#529-product-marketing-requirements)
- [6. Accessible Process Requirements](#6-accessible-process-requirements)
    - [6.1. Solicit Feedback](#61-solicit-feedback)
    - [6.2. Testing](#62-testing)
    - [6.3. Sound Design](#63-sound-design)
    - [6.4. Language and Text Design](#64-language-and-text-design)
- [7. Accessible Technology Platform Requirements & Responsibilities](#7-accessible-technology-platform-requirements--responsibilities)
    - [7.1. Setup](#71-setup)
- [8. Accessible Software Library Requirements & Responsibilities](#8-accessible-software-library-requirements--responsibilities)
- [9. Accessible Platform Requirements & Responsibilities](#9-accessible-platform-requirements--responsibilities)
    - [9.1. Developer Tools](#91-developer-tools)
    - [9.2. Accessibility Test Tools](#92-accessibility-test-tools)
    - [9.3. Platform Privacy](#93-platform-privacy)
    - [9.4. Platform Security](#94-platform-security)
    - [9.5. Platform Save Settings](#95-platform-save-settings)
    - [9.6. Platform Visual](#96-platform-visual)
        - [9.6.1. Platform Contrast Preference](#961-platform-contrast-preference)
        - [9.6.2. Platform Light / Dark Mode Preference](#962-platform-light--dark-mode-preference)
        - [9.6.3. Platform Background Detail Preference](#963-platform-background-detail-preference)
    - [9.7. Platform Audio](#97-platform-audio)
        - [9.7.1. Platform Background Audio](#971-platform-background-audio)
    - [9.8. Platform Pause](#98-platform-pause)
    - [9.9. Speech Synthesis](#99-speech-synthesis)
    - [9.10. Platform Subtitle and Closed Captions](#910-platform-subtitle-and-closed-captions)
    - [9.11. Platform Typefaces](#911-platform-typefaces)
        - [9.11.1. Platform Supported Typeface Requirements](#9111-platform-supported-typeface-requirements)
    - [9.12. Input Remapping](#912-input-remapping)
    - [9.13. Tab-based Navigation](#913-tab-based-navigation)
- [10. Accessible Development Environment and Tools Environment Requirements](#10-accessible-development-environment-and-tools-environment-requirements)
- [11. Accessible Technology Requirements](#11-accessible-technology-requirements)
    - [11.1. Access to Broadband](#111-access-to-broadband)
    - [11.2. Access to Devices](#112-access-to-devices)
- [12. People Categories](#12-people-categories)
- [13. Glossary](#13-glossary)
    - [13.1. Monaural / Monophonic / Mono Audio](#131-monaural--monophonic--mono-audio)
    - [13.2. Stereophonic / Stereo Audio](#132-stereophonic--stereo-audio)
    - [13.3. Binaural Audio](#133-binaural-audio)
    - [13.4. Surround Sound](#134-surround-sound)
    - [13.5. Spatial Audio](#135-spatial-audio)
    - [13.6. Monoscopic Video](#136-monoscopic-video)
    - [13.7. Stereoscopic / Stereoscopy Video](#137-stereoscopic--stereoscopy-video)
    - [13.8. Two-dimensional (2D)](#138-two-dimensional-2d)
    - [13.9. Two-point-five dimensional (2.5D)](#139-two-point-five-dimensional-25d)
    - [13.10. Three-dimensional (3D)](#1310-three-dimensional-3d)
    - [13.11. Extended Reality (XR)](#1311-extended-reality-xr)
    - [13.12. Virtual Reality (VR)](#1312-virtual-reality-vr)
    - [13.13. Augmented Reality (AR)](#1313-augmented-reality-ar)
    - [13.14. Mixed Reality (MR)](#1314-mixed-reality-mr)
    - [13.15. Surface Computing](#1315-surface-computing)
    - [13.16. Spatial Computing](#1316-spatial-computing)
    - [13.17. Graphical User Interface](#1317-graphical-user-interface)
    - [13.18. User Experience (UX)](#1318-user-experience-ux)
    - [13.19. Input Modalities](#1319-input-modalities)
    - [13.20. Output Modalities](#1320-output-modalities)
    - [13.21. Captions, Subtitles, and Audio Description](#1321-captions-subtitles-and-audio-description)
        - [13.21.1. Subtitles](#13211-subtitles)
        - [13.21.2. Subtitles for D/deaf and Hard of Hearing (SDH)](#13212-subtitles-for-ddeaf-and-hard-of-hearing-sdh)
        - [13.21.3. Non-SDH Subtitles (Traditional Subtitles)](#13213-non-sdh-subtitles-traditional-subtitles)
    - [13.22. Captions](#1322-captions)
        - [13.22.1. Closed Captions](#13221-closed-captions)
        - [13.22.2. Open Captions](#13222-open-captions)
        - [13.22.3. Immersive Captions](#13223-immersive-captions)
        - [13.22.4. Audio Description](#13224-audio-description)
- [14. References](#14-references)

<!-- /TOC -->

## 4. Definitions

### 4.1. Metaverse

Definition of *metaverse*.

### 4.2. Accessibility

Definition of *accessibility*.

### 4.3. Inclusive design

Definition of *inclusive design*.

### 4.4. User experience

Definition of *user experience*.

## 5. Accessible Product Design Requirements & Responsibilities

Prescriptive Guidelines for creating products and experiences.

### 5.1. Comfort

#### 5.1.1. Sensory Overload

- Players find the visual and sound effects to be enjoyable, including those with sensory sensitivity.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.1.2. Motion Sickness

- Players do not feel motion sickness or related discomfort when playing.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Avoid VR simulation sickness triggers.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-vr-simulation-sickness-triggers/)

#### 5.1.3. Green Room

- Players have time and space to learn and practice game play.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.1.4. Content Comfort

- Players are warned about mature, graphic or disturbing content before being exposed directly to it.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Provide an option to disable blood and gore.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-an-option-to-disable-blood-and-gore/)

#### 5.1.5. Haptics

- Players can control the use of haptics.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- If haptic feedback is a supported feature, players should have the ability to:

  - Turn off the feedback.

  - Adjust the strength of the feedback.

  - Use other means of feedback. Haptic feedback shouldn't be the only method of conveying information. It should be accompanied by visual and auditory indicators.

- Consider adding haptic cues as an optional, additional channel for important visual or audio information.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/110#implementation-guidelines)

- Include toggle/slider for any haptics.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-toggle-slider-for-any-haptics/)

### 5.2. Mobility & Body Mechanics

#### 5.2.1. Settings

- Allow users to configure usability preferences when initially setting up their XR experience.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Allow gameplay to be fine-tuned by exposing as many variables as possible.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-gameplay-to-be-fine-tuned-by-exposing-as-many-variables-as-possible/)

#### 5.2.2. Height

- Players with varying heights and/or seated can comfortably play.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Experience enables adjustable in-app player height.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

#### 5.2.3. Weight

- Be mindful of a person's ability to carry unsupported weight on their head or in their hands for extended periods.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

#### 5.2.4. Body Position

- Players can play seated and are comfortable with any physical stretching or body positions.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Applications that can be used in sitting or standing mode should provide a setting to enable users to perform all interactions and access information from a fixed position.

    [Meta | VRC.Quest.Accessibility.9](https://developer.oculus.com/resources/vrc-quest-accessibility-9/)

- Experience works while seated in a swivel chair position.

- Experience works while seated in a fixed position.

- Experience works while seated at a 45° position.

- Experience works while laying flat on one's back.

- Experience works with head tracking disabled.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Where possible, allow for play to be experienced from a bed, or a fixed seated location, or a wheelchair.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- Allow users to access the experience from a seated, reclining, or stationary position, if the application otherwise would require standing or body movements to access its full content.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Support different body sizes by following the *Yoda/Chewbacca Principle*:

  - Ensure someone that is Yoda's size (0.66 m / 2 ft 2 in.) can use the experience.

  - Ensure someone that is Chewbacca's size (2.3 m / 7 ft 6.55 in) can use the experience.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

#### 5.2.5. Handedness

- Players who are right-handed and left-handed can comfortably play.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Ensure controls and gestures are ambidextrous.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

#### 5.2.6. Single Handed

- Players can play the game comfortably with one hand.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Applications should provide an option to be played with one hand and/or controller. Ideally, the user can configure their controller options.

    [Meta | VRC.Quest.Accessibility.4](https://developer.oculus.com/resources/vrc-quest-accessibility-4/)

- Experience works with one controller.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

#### 5.2.7. Buttons Use

- Experience works with no buttons.

- Experience works with minimal button use.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Avoid requiring buttons to be held down or provide an alternative control scheme such as toggling buttons rather than holding them down. This is so a person in a wheelchair can have their hands free while moving.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- Allow users to map several actions to a single controller button or action to be able to complete complex multi-step actions or choices in a sequence.

- Allow users to reduce the number of required controls in order to limit the number of things they have to do to accurately complete any objectives contained in the program.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Avoid repeated inputs (button mashing/quick time events).

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-repeated-inputs-button-mashingquick-time-events/)

#### 5.2.8. Locomotion

- Players can play the game without being required to physically walk.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Applications should provide the user with the option to rotate their view without physically moving their head/neck.

    [Meta | VRC.Quest.Accessability.7](https://developer.oculus.com/resources/vrc-quest-accessibility-7/)

- Applications should support multiple locomotion styles when possible. This includes, but is not limited to, teleportation, free locomotion, and snap turning.

    [Meta | VRC.Quest.Accessibility.8](https://developer.oculus.com/resources/vrc-quest-accessibility-8/)

- Application supports smooth locomotion

- Application supports smooth turning.

- Application supports teleportation

- Application supports snap turn control.

- Supports passive mode.

- Supports anti-nausea vignette / "blinders".

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Supports co-pilot assistive mode.

- Supports standing-only experience.

- Supports room-scale experience.

- Supports world-scale experience.

    [MSF Accessibility Exploratory Group](https://metaverse-standards.org/domain-groups/)

- People with reduced range of motion may need small, precise movements to be amplified.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- Avoid any sudden unexpected movement or events.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-any-sudden-unexpected-movement-or-events/)

- Avoid (or provide an option to disable) any difference between controller movement and camera movement.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-or-provide-option-to-disable-any-difference-between-controller-movement-and-camera-movement-such-as-weaponwalk-bobbing-or-mouse-smoothing/)

#### 5.2.9. Object Pickup

- Players can comfortably carry and put down objects with one or two hands.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.2.10. Menu Access

- Players can access and read menus easily.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.2.11. Controls

- Players can remap controllers as needed.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Allow users to receive assistance in some aspects of the program by enabling a separate controller or sensor

- Enable users to skip or bypass challenging or timed experience while still allowing them to progress in the app.

- Allow remapping of controls onto alternate controllers, sensors, or keyboards.

- Allow remapping of controls on the standard controller to ensure the user can reach the necessary controls.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Allow controls to be remapped / reconfigured.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-controls-to-be-remapped-reconfigured/)

- Ensure controls are as simple as possible, or provide a simpler alternative.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-controls-are-as-simple-as-possible-or-provide-a-simpler-alternative/)

- Offer a means to bypass gameplay elements that aren’t part of the core mechanic, via settings or in-game skip option.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/offer-a-means-to-bypass-gameplay-elements-that-arent-part-of-the-core-mechanic-via-settings-or-in-game-skip-option/)

#### 5.2.12. Dexterity

- Players can comfortably play without repetitive, uncomfortable, sustained, or precise movements.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.2.13. Hand Tracking

- Experience works with hand tracking.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Allow users to select controller-free hand tracking as their primary way of manipulating the interface and progressing through the app.

- Allow users to directly "touch" a nearby object (absolute interactions).

- Allow users to control or manipulate objects further away (relative interactions).

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

#### 5.2.14. Eye Tracking

- Allow users to select eye tracking as their primary way of manipulating the interface and progressing through the app.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

#### 5.2.15. Body Tracking

- Do not rely on motion tracking of specific body types.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/do-not-rely-on-motion-tracking-of-specific-body-types/)

#### 5.2.16. Neural Interfaces

- Neural interfaces must keep user information and interactions secure and private. Users must opt-in to share their information.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

#### 5.2.17. Dynamic Foveated Rendering

- Use eye tracking to enable dynamic foveated rendering that moves the user's field of vision as the user's eyes move.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

### 5.3. Cognitive

- Allow the game to be started without the need to navigate through multiple levels of menus.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-the-game-to-be-started-without-the-need-to-navigate-through-multiple-levels-of-menus/)

#### 5.3.1. Difficulty

- Players can feel comfortable with the difficulty of the game.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Offer a wide choice of difficulty levels.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/offer-a-wide-choice-of-difficulty-levels/)

- Allow difficulty to be altered during gameplay, either through settings or adaptive difficulty.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-difficulty-level-to-be-altered-during-gameplay-either-through-settings-or-adaptive-difficulty/)

#### 5.3.2. Complexity

- Players can quickly and easily start the game and navigate the menus and user interface.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Ensure the experience is focused.

  - Reduce the number of features in your application so that they account for the needs of the people using the application in a particular scenario.

  - Make sure the set of features is focused on particular tasks and that those tasks are clear to people.

  - Limit similar choices to reduce complexity and the time needed for people to make decisions.

    - Duplicate controls and interface elements that appear to offer the same functionality are disruptive.

    - When you need to provide a large number of choices, use the ElementMenu.

      - Simple, organized, and hierarchical structure.

      - People can tap or slide to navigate through the menu system.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- Users may at times have difficulty quickly and accurately reacting to prompts, experience options, and/or physical or reflex challenges due to mobility, vision, auditory, or cognitive disabilities.

- Enable users to increase the time allotted for making decisions or completing challenges.

- Enable users to pause the app or game to set up action sequences for tasks that require several steps to ensure they can accurately respond to each challenge.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Enjoy a simple, clear narrative structure.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/employ-a-simple-clear-narrative-structure/)

- If using a long overarching narrative, provide summaries of progress.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/if-using-a-long-overarching-narrative-provide-summaries-of-progress/)

- Ensure no essential information (especially instructions) is conveyed by text alone, and is reinforced with visuals and/or speech.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-no-essential-information-especially-instructions-is-conveyed-by-text-alone-reinforce-with-visuals-andor-speech/)

- Provide an option to turn off / hide all non-interactive elements.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-an-option-to-turn-off-hide-all-non-interactive-elements/)

#### 5.3.3. Memory

- Players with varying levels of memory feel comfortable playing the game.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.3.4. Assistance

- Allow users to choose to have the app assist them in navigating the interface and in helping them to complete any tasks, such as might occur in workplace training programs or gaming.

- Allow users to automate some actions to reduce the number of physical actions they must make within an app.

- Allow the user to receive assistance in orienting themselves in the experience or to receive more context about their progression in the app. Such options should provide:

  - Information about where they are in the virtual space.

  - What they can or should do next.

  - Their current progress in the app.

- Provide in-app prompts to help the user progress through the experience such as:

  - Reminders

  - Help topics

  - Introductions to new features.

- Provide training opportunities for users to experiment with the interface and control configurations so they can learn the potential challenges they may face and choose their settings accordingly.

- Allow users to review their in-app objectives – both completed and future – to reorient them in the application and ensure they can effectively progress.

- Allow users to hide distracting and non-critical interface components, including visual, audio, and/or animated components to ensure they are able to focus on the most essential information being communicated to them.

- Allow users to review the controller configurations.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Include interactive tutorials.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-tutorials/)

- Indicate / allow reminder of current objectives during gameplay.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/indicate-allow-reminder-of-current-objectives-during-gameplay/)

- Indicate / allow reminder of controls during gameplay.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/indicate-allow-reminder-of-controls-during-gameplay/)

- Include assist modes such as auto-aim and assisted steering.

    >[!NOTE]
    >Questions of multiplayer fairness can be addressed through matchmaking preferences.

    [Games Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-assist-modes-such-as-auto-aim-and-assisted-steering/)

#### 5.3.5. World Exploration

- Allow users to familiarize themselves with the app and its various interfaces and input needs to help users feel more comfortable taking an active part in the program and help them understand and experiment with the interface and the environment prior to utilizing the app, and to set preferences.

- For apps that include challenge, puzzle, or gaming features, this option will allow users to simply experience the app and its virtual world without having to take on challenges that may prove difficult or frustrating.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Include a means of practicing without failure, such as a practice level or sandbox mode.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-a-means-of-practicing-without-failure-such-as-a-practice-level-or-sandbox-mode/)

#### 5.3.6. Speed

- Include an option to adjust the game speed.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-an-option-to-adjust-the-game-speed/)

### 5.4. Context

#### 5.4.1. Classroom support

- Players are able to play the game within the constraints of a classroom environment.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.4.2. Moderation

- Players are able to be locked into or out of particular features (i.e., age-gated features like voice chat or parent or teacher-controlled features).

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.4.3. General (Saving Settings)

- Players can save games and/or profile settings.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Provide gameplay thumbnails with game saves.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-gameplay-thumbnails-with-game-saves/)

- Ensure that all settings are saved/remembered.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-that-all-settings-are-savedremembered/)

- Provide a manual save feature.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-manual-save-feature/)

- Provide an autosave feature.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-an-autosave-feature/)

- Allow settings to be saved to different profiles at the game level.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-settings-to-be-saved-to-different-profiles-at-either-game-or-platform-level/)

#### 5.4.4. Space Constraints

- Players with minimum physical space can play the game.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

### 5.5. Language & Communication

#### 5.5.1. Reading Comprehension

- Players with varying reading levels and speeds can read and understand the text.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Allow users to reduce the speed of the app or increase the time allotted for making decisions or completing challenges.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Use simple clear language.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/use-simple-clear-language/)

- Allow players to progress through text prompts at their own pace.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-players-to-progress-through-text-prompts-at-their-own-pace/https://gameaccessibilityguidelines.com/allow-players-to-progress-through-text-prompts-at-their-own-pace/)

- Highlight important words.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/highlight-important-words/)

- Provide pre-recorded voiceovers for all text, including menus and installers.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-full-internal-self-voicing-for-all-text-including-menus-and-installers/)

- Allow all narrative and instructions to be replayed.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-all-narrative-and-instructions-to-be-replayed/)

- Use symbol-based chat (e.g., smileys, etc.)

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/use-symbol-based-chat-smileys-etc/)

#### 5.5.2. Hearing

- Audio considerations for users with hearing impairments fall under two main brackets; allowing control of the audio balance and providing communication redundancy with visual feedback.

- Examples include:

  - Providing separate volume controls for music, effects, and speech.

  - Offering options for communicating information shared audibly, through visual / haptic cues

  - Ensure the experience is completable without audio

  - Optional "turn up" of the universal tell indicators.

  - Offering the option of a mono downmix.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

#### 5.5.3. Subtitles / Closed Captions

- Players with limited hearing or who prefer reading can comfortably read what would be heard.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Experience works with closed captions and/or subtitles.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Subtitles (text equivalents for speech) are provided for all spoken content.

- Identify the speaker, and use visual spatial indicators to indicate which direction the speaker's voice is coming from if it's not immediately clear.

  - The speaker's name should be identified in the subtitle line each time a new speaker begins talking. Once the speaker's name is established, the speaker name does not have to re-appear on every subsequent subtitle line while the same speaker is talking. The name of the speaker only needs to appear again in the subtitle line when there is a change in speakers, or if a significant pause (greater than 1-2 minutes) has taken place during the same speaker's dialogue.

  - Color can be used to distinguish who is speaking. However, color should be used in conjunction with another means of portraying information, such as text.

    >[!NOTE]
    >In scenarios where the speaker is an unidentified “narrator,” and there are no other speakers, identifying “narrator:” in the subtitle or caption text is not required.

  - Players can adjust the option before starting the game, or subtitles are enabled by default. This ensures that players don't get dropped into a long introduction cinematic without being able to follow along.

  - Captions (text equivalents for all audio) are provided for all important sounds that aren't already communicated visually. Spatial indication (like arrows next to the text) should be provided to indicate which direction a sound is coming from if it's not immediately clear (for example, if the sound is coming from something occurring offscreen).

  - Subtitles and captions can be turned on or off at any time and configured easily through a discoverable setting.

  - Allow different types of caption information (like main character dialogue, background character dialogue, or ambient noises) to be toggled on or off independently of one another.

  - Whenever possible, the title should use the caption/subtitle settings that are configured by the player at the platform level by default.

- Subtitle and caption text should conform to the following standards.

  - Size: Text size should meet the minimum defined pixel height by default as defined in [XAG 101: Text display](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101). (The ability to configure text to be smaller or larger than the default minimum in the settings is also beneficial to players.)

    >[!NOTE]
    >Unlike static text in menus, subtitle and caption text for spoken dialogue is typically only displayed on-screen for short periods of time. Given this, developers are encouraged to offer larger minimum default sizes for caption and subtitle text to facilitate ease of rapid reading.

  - Adjustable size: Scalable to a large size (minimum of 200 percent of minimum default text size). For more information, see XAG 101: Text display.

  - Spacing: Readability is improved when words and lines of text aren't very close to each other. Avoid offering a font that has small spacing between the characters.

  - Length: Avoid long lines of text (more than 40 characters), especially when the dialogue is fast. When text appears rapidly, longer lines of text are harder to read than shorter ones. Show no more than two lines of subtitles on screen at a time (three can be used in exceptional cases).

    - When possible, line breaks should be entered manually (as opposed to automatic wrapping or splitting) to ensure that breaks occur at editorially sensible points.

  - Case: Font should be in mixed case. It's much easier to read than all the same case. For example, "Hello. How have you been?" versus "HELLO. HOW HAVE YOU BEEN?"

  - Sans serif: Ensure that at least one san serif font option is available for subtitles and closed captions.

  - Background color: Players should be able to place a solid background behind subtitle and caption text to ensure readability of that text, regardless of the game's background. (For example, white text presented over light desert sand looks virtually invisible to the player.) The color of this background should be configurable by the player.

  - Background opacity: Players should be able to adjust the opacity of the background on a scale from 0 to 100 percent. This supports players who might require high contrast as well as others who might find an opaque background obtrusive.

  - Placement: Ensure that important UI/gameplay elements are designed to avoid being obscured by subtitles when scaled to the largest size. This can generally be achieved by ensuring that placement is toward the bottom of the screen.

- Provide a visual simulation of what subtitle and caption presentation options will look like based on the player's current configuration settings.

  - If possible, this preview should be shown in a realistic game context.

- Caption and subtitle information should persist during screen recordings, captures, and other user-generated content (UGC). Other players viewing that content can choose to display it.

- Full transcripts of FMVs should be made available via an accessible website.

- Sign language interpretation is provided for scripted in-game cutscenes and prerecorded/pre-rendered sequences of media that include speech, such as full motion videos (FMV’s).

  - Signing requires localization, just like spoken languages do. For example, American Sign Language, British Sign Language, and Japanese Sign Language are all vastly different from one another.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/104#implementation-guidelines)

- In addition to audio considerations, subtitles should be available for people with hearing impairments, as well as people using Magic Leap 1 in environments with high levels of noise, and non-native English speakers. When developing with this feature, we recommend these initial considerations:

  - Using clear, high contrast text on an additive display

  - Exploring placement and frame of reference for subtitles (relative to the user, are they in world, are they attached to an on screen speaker, etc.).

  - Adding relevant non-dialogue information such as environmental noises, music and sound effects and non-verbal character sounds.

  - Support adjustable font size.

  - Consider accessibility-friendly typefaces such as the Dyslexie font, designed while taking the different characteristics of dyslexia into consideration.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- Provide subtitles or captions for audio features.

- Allow users to choose where to place captions and allow them to move them to ensure other visual aspects of the app are observable and unobscured.

- Allow users to change the subtitle and captions font as well as the colors.

- Allow users to change subtitle and caption background colors and transparency.

- Subtitle and captions should clearly indicate or label which speaker is talking.

- Allow users to turn on/off subtitles and closed captions at any time.

- Developers should consult [U.S. Federal Communications Commission (FCC) | Closed Captioning on Television](https://www.fcc.gov/consumers/guides/closed-captioning-television#:~:text=Complete%3A%20Captions%20must%20run%20from,edge%20of%20the%20video%20screen) and [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21/) for more details on captioning best practices.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Provide an audio description track.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-an-audio-description-track/)

- Provide subtitles for all important speech.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-subtitles-for-all-important-speech/)

- If any subtitles / captions are used, present them in a clear, easy to read way.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/if-any-subtitles-captions-are-used-present-them-in-a-clear-easy-to-read-way/)

- Provide subtitles for supplementary speech.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-subtitles-for-supplementary-speech/)

- Ensure subtitles/captions are or can be turned on before any sound is played.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-subtitles-captions-are-or-can-be-enabled-before-any-sound-is-played/)

- Provide captions or visuals for significant background sounds.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-captions-or-visuals-for-significant-background-sounds/)

- Provide a visual indication for who is currently speaking.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-visual-indication-of-who-is-currently-speaking/)

- Allow subtitle/caption presentation to be customized.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-subtitlecaption-presentation-to-be-customised/)

- Ensure that subtitles/captions are cut down to and presented at an appropriate words-per-minute for the target age-group.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-that-subtitlescaptions-are-cut-down-to-and-presented-at-an-appropriate-words-per-minute-for-the-target-age-group/)

#### 5.5.4. Sign Language

- Developers should consider augmenting captions with the persistent display of sign language interpretation within their app.

- Allow users to choose where to place sign language interpretation and allow them to move them to ensure other visual aspects of the app are observable and unobscured.

- Allow users to turn on/off sign language interpretation at any time.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Provide signing.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-signing/)

#### 5.5.5. Language Localization

- Players who speak a language other than the supported language can play the game.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.5.6. Language Input

- Players with varying typing, clicking and speaking (input) speeds and abilities can comfortably play the game.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.5.7. General Accessibility Options Easy to Find

- Players can easily learn about accessibility settings/features in your game and find them.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

### 5.6. Sensory

#### 5.6.1. Visual

- Players with varying vision can understand and play the game comfortably.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Applications should enable people to edit their display settings such as brightness and contrast to accommodate their visual needs.

    [Meta | VRC.Quest.Accessibility.5](https://developer.oculus.com/resources/vrc-quest-accessibility-5/)

- Make interactive elements easy to identify.

  - Make sure visual indicators of touch content are accurate so that people are not misled to touch something that isn’t interactive

    - For example, a disabled button must be made visually distinct from enabled buttons.

  - The larger the interface elements, the more quickly a person can identify it as interactive.

    - Use depth to help indicate whether or not an object is interactive.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- Across the population, many users have visual impairments which require consideration for content developers. Here are three categories of impairments to consider:

  - Please consider color blind individuals when designing your content. Most color blind individuals are red/green color blind. A smaller proportion are blue/yellow color blind. To aid these individuals, choose image layouts that are discriminable in grayscale. It is advised to additionally use other cues such as shape, labels and haptics.

  - Many individuals have reduced visual acuity. This means that they cannot read small text or discern fine details in content. Consider providing pre-recorded voice over for all text, or a text to speech engine.

  - Some users have photosensitive epilepsy which can be triggered by certain types of visual content. Take care to avoid high contrast flickering content in your content scenes.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- Provide users the option to remove or reduce background visual detail so that they may better distinguish the most important activities of tasks in the application.

- Enable users visual loss to skip or bypass challenging or timed experience while still allowing them to progress in the app.

- Allow users to magnify or reduce objects and text to make them larger or smaller.

- Allow users to change fonts for more easily readable text.

- Allow users to change the brightness levels in the app.

- Allow users to employ peripheral maps to show objects outside the field of vision.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Avoid flickering images and repetitive patterns.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-flickering-images-and-repetitive-patterns/)

- Provide an option to turn off / hide background movement.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-an-option-to-turn-off-hide-background-movement/)

- Provide high contrast between text/UI and background.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-high-contrast-between-text-and-background/)

- Avoid placing essential temporary information outside the player's eye-line.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-placing-essential-temporary-information-outside-the-players-eye-line/)

- Ensure that all important supplementary information (eg. the direction you are being shot from) conveyed by audio is replicated in text / visuals.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-that-all-important-supplementary-information-eg-the-direction-you-are-being-shot-from-conveyed-by-audio-is-replicated-in-text-visuals/)

#### 5.6.2. Color Blindness

- Players with varying ability to distinguish certain colors can understand and play the game comfortably.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Applications should either provide color blindness options, or use other techniques such as combining color and pattern for easy visual distinction.

    [Meta | VRC.Quest.Accessibility.6](https://developer.oculus.com/resources/vrc-quest-accessibility-6/)

- Interface elements aren't differentiated by color alone. Distinguishing shapes, icons, labels, and other methods must be used in addition to color for interactive elements.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

- Allow users to add contrasts or edge enhancements to highlight objects and text.

- Allow users to recolor the interface and objects to support users that cannot discern color.

- Provide shapes or symbols alongside meaningful colors.

- Provide textures on objects or elements to help distinguish information in the app.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Provide a choice of text color, low/high contrast choice as a minimum.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-choice-of-text-colour-lowhigh-contrast-choice-as-a-minimum/)

- Ensure no essential information is conveyed by a color alone.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-no-essential-information-is-conveyed-by-a-colour-alone/)

#### 5.6.3. Scrims and Overlays

- A scrim is a translucent gradient layer that aids in making text more readable against background pictures, colors, objects, and other visual elements.

- Use a scrim-like overlay for programs that require readable texts and/or captioning.

- Ensure the scrim do not introduce color gradients that may make text unreadable or prevent users from experiencing the virtual environment.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

#### 5.6.4. Audio

- Players with varying ability to hear can understand and play the game comfortably.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- Application should be playable in its entirety without the use of audio, or provide subtitle options for in-application dialogue and/or sound effects to communicate progress to the user.

    [Meta | VRC.Quest.Accessibility.1](https://developer.oculus.com/resources/vrc-quest-accessibility-1/)

- Games should provide a method for players to adjust the volume of the audio, or mute different types of audio, independently from each other, including but not limited to the following:

  - Music

  - Voice-over

  - Active sound effects (those critical to gameplay like engine noise, gunshots, or footsteps)

  - Background/ambient sound effects (those not critical to gameplay)

  - Narration

  - Voice chat

- Provide an option to enable spatial audio for sound effects, narration, and any other important game sounds that help the player determine the directionality of the audio.

- Provide an option that allows the player to convert stereo audio to mono audio sent to both channels.

- Players should be able to pause audio events, including cinematics with audio.

    >[!NOTE]
    >Events that play for less than three seconds don't need a method to pause playback. Real-time, multiplayer gameplay is exempt from this guideline (players don't need to be able to pause a live multiplayer session).

- The game should include an option to automatically lower or mute game audio when audio output from assistive technologies such as a screen reader is detected.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/105#implementation-guidelines)

- Provide users the option to remove or reduce background audio detail so that they may better distinguish the most important activities of tasks in the application.

- Enable users with hearing loss to skip or bypass challenging or timed experience while still allowing them to progress in the app.

- Allow users to switch between stereo and mono audio.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Provide separate volume controls or mute for effects, speech background audio, and music.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-separate-volume-controls-or-mutes-for-effects-speech-and-background-music/)

- Ensure sound/music choices for each key object/event are distinct from each other.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-sound-music-choices-for-each-key-objects-events-are-distinct-from-each-other/)

- Use surround sound.

    >[!NOTE]
    >Surround sound in this context might more accurately be called *spatial audio*.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/use-surround-sound/)

- Use distinct sound / music design for all objects and events.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/use-distinct-sound-music-design-for-all-objects-and-events/)

- Simulate binaural recording.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/simulate-binaural-recording/)

- Ensure no essential information is conveyed by sounds alone.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-no-essential-information-is-conveyed-by-sounds-alone/)

- Keep background noise to a minimum during speech.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/keep-background-noise-to-minimum-during-speech/)

- Provide a stereo/mono toggle.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-stereomono-toggle/)

#### 5.6.5. Sensory Feedback

- Provide engaging sensory feedback.

- Give feedback that engages people’s senses through visuals, sound, motion, and physical interactions.

  - Include visuals that are pleasing and appropriate for the scenario.

  - Include sounds that are appropriate to the application that help people understand that something has happened.

  - Include visual cues and hints that lead people to discover new places, things, or effects within the application.

    - For example, an application can use animation to teach interactions or hint at functionality.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.6.6. User Interface (UI)

- Text and in-app controls and elements necessary for app progression should be clearly legible. When possible, provide options for increased contrast and/or larger user interface (UI) elements.

    [Meta | VRC.Quest.Accessibility.2](https://developer.oculus.com/resources/vrc-quest-accessibility-2/)

- When possible, the application should provide clarity and direction to the user through a combination of visual, audio, and/or haptic feedback instead of relying on one form of feedback.

    [Meta | VRC.Quest.Accessibility.3](https://developer.oculus.com/resources/vrc-quest-accessibility-3/)

- Experience enabled adjustable menu location.

- Experience provides on-screen instructions.

- Experience provides adjustable user interface (UI) sizing options.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Ensure user actions are reversible.

- Ensure interactive elements look interactive.

- Ensure non-interactive elements do not look interactive.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

- Create a welcoming and friendly application environment that invites people to safely explore and experiment.

- Avoid unintentional or destructive major transitions

  - Require destructive and large changes to be explicitly and intentionally activated by people.

    - For example, the Access Points require intentional input to leave an application or start a new experience. This two-step system makes accidental activation of the Access Points unlikely.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- Allow users to undo or redo actions they've made in error or because of imprecision.

- Let users confirm an irreversible action before it happens.

- Allow users to slow down various aspects of a game or app, such as slower cursors to allow more precise movements to more accurately target menu options, objects, or other features in a user interface (UI).

- Allow users to slow down camera movements.

- Allow users to zoom the camera in or out.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Enable users to adjust the camera's field of view (FOV).

    [James Maki | Inclusive Reality](https://inclusivereality.com)

- Ensure interactive elements / virtual controls are large and well spaced, particularly on small or touch screens

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-interactive-elements-virtual-controls-are-large-and-well-spaced-particularly-on-small-or-touch-screens/)

- Allow interfaces to be rearranged.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-interfaces-to-be-rearranged/)

- Allow interfaces to be resized.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-interfaces-to-be-resized/)

- Provide a macro system.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-macro-system/)

- Allow play in both landscape and portrait

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-play-in-both-landscape-and-portrait/)

- Ensure your experience supports aspect ratios from 6:1 (6.0) to 1:6 (0.1667).

    [James Maki | Inclusive Reality](https://inclusivereality.com)

- Give a clear indication that interactive elements are interactive.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/give-a-clear-indication-that-interactive-elements-are-interactive/)

- If the game engine uses a field of view (FOV) (3D engine only), set an appropriate default for the expected viewing environment.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/if-the-game-uses-field-of-view-3d-engine-only-set-an-appropriate-default-for-the-expected-viewing-environment/)

- If the game uses field of view (FOV) (3D engine only), allow a means for it to be adjusted.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/if-the-game-uses-field-of-view-3d-engine-only-allow-a-means-for-it-to-be-adjusted/)

- Provide a choice of cursor / crosshair colors / designs.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-choice-of-cursor-crosshair-colours-designs/)

#### 5.6.7. User Interface (UI) Navigation

- From the game’s initial launch, ensure that all pathways to the accessibility features/settings menu UI are fully accessible.
This can be done by:

  - Prompting players to configure accessibility settings as the first screen that appears when the game launches. After the player has defined them, any subsequent experiences only need to reflect the accessibility settings that the player made.

  - Meeting all XAGs by default when the game initially launches (for example, text display and contrast ratios meet minimum guidelines, narration and subtitles/captions are enabled by default, and visual distractions are disabled by default).

  - Meeting all XAGs by default when the game initially launches but using platform settings to disable certain items by default, based on the player’s current platform settings (if possible).

    - For example, a player has “Let Games Read to Me” disabled at the Xbox platform level. As a result, the game doesn’t need to launch with in-game narration enabled by default.

    - If the game is unable to read platform settings, narration should be enabled by default for all players.

- The UI navigation order is logical and consistent across the full game.

- The UI is fully navigable by keyboard and controller digital input alone.

- All aspects of the game, including menu UI's and gameplay, are fully navigable by multiple inputs (mouse, eye gaze, voice, keyboard, and controller).

  - Some inputs might not be supported by the platform (for example, eye gaze on Xbox). If platforms support multiple input options, games should ensure that their UIs are also navigable by multiple supported inputs.

- Components that are repeated across multiple pages or screens should appear in the same relative order (the same place in the programmatic sequence) each time that they're repeated.

- If an interface can be navigated sequentially, focusable components should receive focus in an order that's logical and preserves meaning and purpose.

- Support a focus order that's aligned with the meaning or operation of the UI. If the navigation sequence is independent of the meaning or operation, align the focus order with the flow of the visual design.

- After navigating to the last item in the UI/menu structure, the player should be taken back to the first item in the UI/menu structure and vice versa.

    >[!NOTE]
    > This guideline only applies to linear menu structures where focus can be moved EITHER up or down, OR left or right. Menus structures that allow focus to be moved to elements in any direction (such as a menu with focusable items arranged in a 4x4 tile) do not need to loop. We encourage developers to have an option to enable and disable menu looping for all menus.

- There should be more than one way to locate content that's part of a complex set of information that spans multiple pages/screens, such as bestiaries, quest logs, or large inventories.

- If the visual layout of a screen changes (because of UI scaling or resolution change), the order in which elements are navigated should update to maintain consistency with the visual layout.

- Text/UI scaling shouldn't result in having to scroll in two directions to reveal all content.

- When game map UI is scaled or zoomed in on, provide an alternative way to navigate the map that does not require scrolling such as a supplementary text list of points of interest.

- Provide persistent links back to the main menu screen or the initial interactive screen on all submenus.

- If focus can be moved to a UI element of an interface, focus can be moved away from that element by using the same input (keyboard or mouse) method.

  - If doing so requires any means of navigation that's inconsistent with how the rest of the interface is navigated, the UI should provide clear interaction prompts to indicate how focus can be moved away.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/112#implementation-guidelines)

- Ensure that all areas of the user interface can be accessed using the same input method as the gameplay.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-that-all-areas-of-the-user-interface-can-be-accessed-using-the-same-input-method-as-the-gameplay/)

- Provide a pingable sonar-style audio map.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-pingable-sonar-style-audio-map/)

- Provide a voiced GPS.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-a-voiced-gps/)

- Allow easy orientation to / movement along compass points.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-easy-orientation-to-movement-along-compass-points/)

#### 5.6.8. User Interface (UI) Focus Handling

- All UI elements should display a highly visible focus indicator when they receive focus.

  - There are multiple ways to ensure that focus indicators are highly visible. This includes the use of borders around the element, increasing the element's size or font weight upon receiving focus, or combinations of multiple methods to ensure that there is high visibility.

- The visual focus indicator should always be visible on screen. Focus indicators should not become invisible on any focusable element, and it shouldn't move to invisible or offscreen elements.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/113#implementation-guidelines)

#### 5.6.9. User Interface (UI) Context

- All screens and elements on those screens should provide enough context such that a player can understand where they are in the UI hierarchy at any particular time.

- UI context shouldn't change without first being initiated by the player. If a change in context isn't player-initiated, a notification should be provided.

- Any interaction that results in shifting focus to another application should be clearly indicated.

- Ensure that text alternatives (such as narration and tooltips) convey the purpose and operation of the UI components.

- Labels should be visually positioned near the associated element so that the player can derive context.

>[!NOTE]
>The visual association between label and element should also be reflected programmatically for screen narration users. See XAG 106: Screen Narration for detailed information on this topic.

- The features and functionality of the player's experience should be the same for everyone, regardless of their use of assistive technology.

- Players should understand what data is expected to be entered into a form or control without requiring additional navigation to discover this information.

- Components reused in different areas that have the same functionality are identified through consistent iconography, labeling, or text.

- The text of a link alone, independent of its adjacent, surrounding text, should be descriptive enough for the player to understand where the link will take them.

>[!NOTE]
>Screen readers often allow users to skip through links one at a time, without reading the surrounding text. This is why it’s important to ensure the text of the link alone is descriptive.

- For groups of information, the groups should be meaningfully and uniquely labeled so that the player can understand context and differentiate between the groups.

- Provide context-sensitive help for each element on screen where necessary.

- Provide methods to accelerate a player’s ability to provide input to a form.

  - For example, for a list of states (like “California” or “Nevada”), allow the player to enter a few letters to bring up the state. This prevents them from having to scroll through a long list or enter the state's full name.

- Large blocks of text should be split into editorially appropriate sections and have descriptive headings.

- A mechanism is available for displaying specific definitions of words or phrases that are game-specific or used in an unusual or restricted way, including idioms, jargon, acronyms, and abbreviations.

- UI text that is critical to understanding gameplay or managing game settings (text within menu UIs, tutorials, instructions, etc.) should not require a reading ability that's more advanced than a lower secondary education (seven to nine years of school).

  - Narrative text that contributes to the game’s storyline such as journals, character dialogue, other in-game story content, and proper names or titles are not subject to this guideline.

- A visual simulation that depicts how a particular setting or option will alter the player’s UI should be provided.

  - If possible, this preview should be shown in a realistic game environment context.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/114#implementation-guidelines)

- Include contextual in-game help/guidance/tips.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-contextual-in-game-helpguidancetips/)

#### 5.6.10. User Interface (UI) Horizontal

- Use 360° degree application design for horizontal deployments

  - Make sure everyone can use content, avoid facing it toward only one side of the display.

  - Enable people to change the direction content faces. Don't lock content to a particular screen direction.

    - Some customer application proposals may require people to be on specific sides of the screen. This generally limits application usability, so consider it carefully.

      - For example, a collaborative sales application may require a salesperson to always be on one side of the unit and the customers to always be on the opposite side. While this may seem to meet the initial customer need, it will diminish the application as it limits social appeal.

  - If the application is freely oriented (has no top or bottom), enable people to change content orientation within the application.

  - Surface applications must face new content and interface elements to the people using it. Developers can use finger orientation and the direction of activated content and controls to make reasonable assumptions about which way to point new content and elements.

  - If the application still has a distinct top and bottom, give people a way within the application to change the orientation of the entire application.

    - Simple "flip" buttons are prone to accidentally touching them, ruining the experience. The Surface Launcher uses a side handle which requires people to perform a simple, deliberate, action before the grouped content is rotated.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.6.11. User Interface (UI) Vertical

- Use 180° degree application design for vertical deployments.

  - Orient new content and interface elements toward the bottom of the screen.

  - Make sure new content appears right-side up.

  - Understand how people share vertical space.

    - In vertical settings screen space might be sectioned off in columns for several people to use at the same time.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.6.12. User Interface (UI) Direct touch interactions

- In contrast to the graphical user interface (GUI) mouse and keyboard type of interaction, Surface uses touch and gesture interactions to manipulate onscreen content. Simple direct touch interactions help people immediately and intuitively understand the result of their actions, better connecting them to the experience. Using hardware or software buttons to indirectly affect content doesn’t typically give them the same sense of control.

- Direct touch interactions and indirect touch interactions

  - Direct touch interactions are physical movements of virtual content within the application by a finger or physical object. Indirect touch interactions usually rely on application interface chrome or abstract gestures. Examples of indirect touch interactions can include buttons, sliders, menus, and gesturing with symbol drawing. Direct touch interactions are the preferred type of interaction for use in Surface because they help to create more intuitive, content oriented experiences.

    - Do not redefine standard direct touch interactions.

    - Use the manipulation processor in the Surface SDK to always yield the correct results.

      - Move: One or more fingers on an item to move or flick it.

      - Resize-out or enlarge: Two or more fingers on an item are dragged apart.

      - Resize-in or reduce: Two or more fingers on an item are dragged closer together.

      - Single-finger rotate: One finger touches an item and drags it around in a circle so that it rotates.

      - Two-finger rotate: Two or more fingers on an item are dragged in opposite directions along an arc.

      - Pin turn: One finger remains stationary acting as a pivot point while other fingers move around it.

    - Don't use chrome or controls to replace direct touch interactions.

      - For example, do not use a rotate button in place of directly rotating an item with a finger.

- Enable single-finger drag and flick.

  - Enable single finger drag and flick interactions on all movable content.

  - Using a consistent single finger drag and flick makes certain that people can always use basic direct touch interactions with all content.

- Design applications for touch.

  - Interactive elements must be properly sized for finger and object touches.

    - Any item that responds to people's touch, a touch target, must be at least 18 mm in size in all directions (18 mm x 18 mm).

    - Allow at least 3 mm between minimally sized touch targets.

    - Position interactive elements so that hands, arms, and objects covering the screen do not block relevant content surrounding interactive elements.

- Respond to multitouch.

  - Microsoft Surface recognizes and responds to over 50 different touches at the same time.

  - Your application must respond to multitouch hardware capabilities.

  - People expect to use multitouch interactions throughout the experience, not only in self-contained portions of the application.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.6.13. Content Oriented

- Content oriented applications encourage exploration and discovery. Experiences that are content focused are more direct, intuitive and enjoyable for people to use.

- Make content the interface

  - Do not replace direct touch interactions with UI controls such as buttons, menus and sliders.

  - Do not clutter the screen with unnecessary and redundant UI controls and chrome.

  - Do not replace touch as the primary interaction.

    - Do not connect external input devices to a Surface unit in such a way that they replace the primary interaction experience.

    - Applications must support and promote the Surface touch experience, not replace it.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.6.14. Digital Object Behavior

- Onscreen objects should have subtle physics in performing motions, inertia of movement, and natural feeling collisions to help create a sense of consistency.

  - Use interaction metaphors that start with physical manipulation then extend it beyond what is possible in the real world embracing the possibilities of the digital world.

    - For example, in a photos application you may be able to move photos around the screen with a flick (mimicking real world interactions) but you can zoom into the photo with a simple manipulation (only possible in the virtual world).

  - Mimic the real world in your transitions by using notions such as mass, acceleration, friction, viscosity, and gravity.

  - Use inertia on objects and content.

    - This contributes to creating a consistent experience across applications. The inertia processor in the Surface SDK makes inertia simple to implement. The processor includes two types of inertia: realistic and goal-oriented.

#### 5.6.15. Responsiveness

- Always respond to touch.

  - People might try something that does not work, and the resulting visual feedback should help them learn, resolve problems or encourage them in a positive direction.

- Guide people with visual hints and just-in-time chrome

  - Give people subtle visual hints as to what the interaction should be.

    - For example, the Launcher rotate handles use a subtle visual hint showing the type of touch interaction that should be used to rotate the control.

  - Use just-in-time chrome to guide interaction. Just-in-time chrome means that controls reveal themselves only when needed.

    - For example, in a photos application, ElementMenu should appear upon touching an individual photo rather than being onscreen at all times.

- Ensure instant gratification and a sense of success

  - Visually acknowledge touch.

    - Touch visualizations quickly and successfully allow your application to visually acknowledge touch.

      - All content must respond to touch and must do so immediately and visually. People need feedback that they have successfully touched an object.

      - Touch can be acknowledged with depth, glows, or other visualizations.

  - Applications must immediately respond to touch input.

  - Let people control the experience and do not provide too many automated actions.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

### 5.7. Visual & Motion Design

#### 5.7.1. Animations

[Add information here.]

#### 5.7.2. Transitions

- Transitions must be fluid and smooth

- Smooth transitions give the user context about where they are in the experience.

  - Make every transition fluid to keep people in a continuous flow.

  - Avoid jarring transitions.

    - Smooth transitions maintain continuity and help people stay oriented.

  - Nothing should abruptly appear or disappear.

  - Every object and visible property change must smoothly animate and transition into and out of existence, or between changes.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.3. Orientation & Layout

- Laying out visual elements on Surface provides interesting opportunities with the 360º degree nature of the multiuser interface. In most Surface applications, any person from any side of the display should at all times be able to read, understand, and interact with any object on the screen.

- There is often no “absolute direction” within Surface applications; there is no explicit top, bottom, left, or right. Instead, it is best to think in terms of position relative to each person, where an object might simply be rotated or placed towards or away from the people using the device.

- Application orientation

  - When an application is launched, ensure that its default orientation is beneficial to most people around the device.

  - In a horizontal deployment:

    - If an application can have its content freely oriented, that content should be oriented in a way that indicates to people that the content is rotatable and movable.

  - If an application must be facing in one particular direction, it should follow the same orientation as the Launcher.

  - In a vertical deployment:

    - The Launcher can only be oriented towards the bottom of the screen and applications should follow the same orientation as the Launcher.

- Grid-free layouts

  - Most visual designers have learned to create layouts based on grids. The 360º degree nature of Surface is great for laying out applications without a global, or screen wide, grid system. This requires a fresh perspective on visual layout; the Surface SDK ScatterView control is a quick and easy way to create grid-free global layouts. It encourages people to organize and explore content. ScatterView acts as an invisible container for onscreen objects, enabling some content to be oriented towards each edge of the screen by default, which encourages curiosity, direct touch interactions, and exploration.

  - Layouts don’t need to be grid-free all the time. For example, the LibraryContainer control is a quick way to create order in a local section of a grid-free layout so that content may be easily sorted, filtered, and organized. Applications can also let people decide when to switch between different visual organization methods.

- Gridded layouts

  - Grid based layouts still have their place and can be useful in certain Surface applications. Gridded layouts are ideal for productivity or focused activities, linear sorting of data, or simply to create a visual rhythm. Layout grids for Surface experiences can be local (specific to a particular content item) or global (screen-wide).

    - Using local grids

      - These are layout systems that apply to specific objects, not to the screen as a whole. A particularly useful implementation of local grids is within a ScatterView item; your application can enable 360º degree experiences with ScatterView, but the local grid can be used within ScatterView to give a feeling of organization and structure.

    - Using global grids

      - Global grids determine the arrangement of content and controls for the entire application. Screen wide global grids are useful when duplicate controls are offered to each person, or to each side of the Surface screen.

      - While permitting easy scanning and organization, they often force the entire UI to be oriented towards one side of the screen and make it difficult for people to collaborate. If you are laying out elements on a global grid, give careful consideration to content orientation for every person on each side.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.4. Depth

Using the z-axis, or depth, for content organization and visual prioritization can be very powerful. Depth helps separate foreground elements from the background and can also provide clear separation between interactive elements and non-interactive elements. The Surface interface uses depth throughout the experience and in transitions between various states such as Attract, Launcher, and applications.

- Use depth to show priority, order, or focus among content items.

- Keep apparent depth shallow, subtle, and elegant.

- Use depth to acknowledge successfully touched objects and controls. Give the illusion of content floating toward a finger to register a successful touch, reserving the highest level of depth for those objects actively being touched.

- Use depth within content and controls to visually indicate touchable regions.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

##### 5.7.4.1. Creating Depth Using 2.5D

- 2.5D is typified by using techniques that simulate or create the illusion of depth without actually requiring 3D geometries. The various techniques can be done without specialized 3D tools using XAML and the Windows Presentation Foundation (WPF) in a high performance way.

  - Scale: Scale can be used to simulate depth, especially when combined with other techniques. Scaling is an ideal way to register successful touch input; a slight increase in scale (or the illusion thereof) gives the impression of an object being magnetized to someone’s finger. Large differences in scale between different levels of depth can lead to an appearance of an extremely deep background. Use small, subtle changes in scale to keep people immersed in the experience.

  - Drop Shadows: Subtle drop shadows are an easy and effective way to indicate depth, but it is important not to make them too heavy. Dark shadows can obscure content below, and very large offsets can make objects feel disconnected from the Surface display.

  - Transparency: Transparency can show depth by allowing objects on lower levels to show through objects above them. This technique is good for a small number of objects onscreen at the same time as transparency can be computationally expensive to render.

  - Depth Cueing: Depth cueing uses tinting, saturation reduction, and/or contrast reduction to simulate distant objects. Subtle reductions in brightness to convey depth and object focus can be quite effective.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

##### 5.7.4.2. Creating Depth Using 3D

- True 3D uses rendered three-dimensional geometries in real time. This enables realistic rotation of cubes, spheres, custom 3D models, and so on. While 3D can be authored in XAML and delivered using WPF, it can adversely impact application performance. True 3D is best created and delivered on Surface using XNA, the core Microsoft 3D and gaming engine.

- True 3D offers many opportunities for interface innovation, but use caution when designing 3D content. Controlling a 3D object on a two-dimensional touch surface can be difficult and confusing. 3D should usually be avoided for the creation of controls, as any text or labels on 3D surfaces can become difficult to read.

- Consider using 3D depth not to describe onscreen objects, but instead as a virtual space to guide people through the application.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

##### 5.7.4.3. Depth as a Visual Hint

- Depth can also be used to indicate interactive zones for touch input. This helps people understand that touching in one region will have a different result than touching in another. For example, the header or title bar of a content item is likely to be dragged, but a list item within that object will scroll when dragged. Making one portion of a control appear above or beneath other elements within that control can help people identify these zones and make their purpose easier to understand.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.5. Shape and Form

- The shape and form of Surface content should visually indicate its function.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.6. Texture

- Generally, using textures as pure decoration is not recommended for Surface experiences. Ornamental textures tend to detract from content, which should always be at the core of the experience. Textures used for purely aesthetic reasons typically create experiences that are not authentically digital.

- There may be certain applications where textures themselves are the content. If texture must be used in your application, keep them minimal, consistent, and always stay focused on encouraging touch and exploration.

- While textures can act as visual hints to help people use the application, many other visual design techniques can achieve the same goal: negative space, form, shape, color, and more. Explore alternatives to using textures as visual hints.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.7. Colors

- Designers should follow established color design guidelines, and take into account the specific requirements of the brands they are handling. There are some additional guidelines that optimize color reproduction for the Surface display.

  - Proof all colors on Surface during the design process; iterative proofing is the best way to achieve consistency and optimize brightness and color for the Surface screen. Do not rely on a desktop monitor for proofing.

  - Never use pure white as a background color.

  - Bright or saturated tones are best in smaller regions to reduce eye fatigue.

  - High contrast, such as pure black on pure white, reduces the effectiveness of anti-aliasing (the subtle edge blending of foreground elements onto the background), making text look harsh and introducing a jagged stair-stepping effect into object and content edges when rotated.

  - Treat the background as a stage against which all action occurs; it should be subtle, calm, and understated.

  - Use subtle gradients cautiously; the reduced color contrast may cause subtle gradients to flatten and appear as one continuous tone.

  - Test gradients on the Surface screen to check for banding.

  - Experiment, iterate, and explore as you become familiar with the Surface display characteristics. Keep an open mind towards taking fresh approaches to a brand’s established color palette.

- Surface colors

  - Surface administrators control the default color scheme of the Surface system. This global color scheme determines the default colors of Surface controls that are rendered in all applications. You can use those same colors to style additional elements in your application. However, you can also override the Surface colors to affect any element in your application that uses those colors.

  - Surface comes with the following four predefined color palettes, defined in the classes of the `Microsoft.Surface.Presentation.Palettes` namespace:

    - `Light palette`

    - `Dark palette`

    - `LightHighContrast palette`

    - `DarkHighContrast palette`

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.8. Typography

- Typography in Surface applications should be elegant and meaningful. With simple interface elements and content at the core of the Surface experience, onscreen text has even more opportunities to act as the interface itself.

- Segoe 360

- Segoe360 is a specially designed typeface for use on Surface. It’s strongly recommended that you use Segoe360 in your applications for the following reasons:

  - Segoe360 comes with three weights: Regular, *Italic*, and **Bold**

  - Segoe360 Regular is a new weight between Segoe UI Regular and Segoe UI Semibold, designed to have better presence on Surface.

  - Characters have been modified for better distinction at all viewing angles, enabling better 360° degree readability. For example, the lowercase `l` is more easily distinguished from a capital `I` and a lowercase `q` is more easily distinguished from a lower case `b` when rotated.

  - Tracking (overall letter spacing) has been increased to be more legible and recognizable onscreen, especially at small sizes.

  - Counters (the enclosed areas in letters like `a` and `e`) have been opened up so they retain their visibility at small sizes.

  - Segoe360 supports Western Europe, Eastern Europe, Turkish, Baltic, Greek and Cyrillic character sets.

- Minimum Segoe360 type sizes:

  - 12 points for interface element labels

  - 16 points for body copy and text

- Selecting typefaces

- Segoe360 is strongly recommended for use in Surface applications, but it may not always fit the needs of a particular brand or scenario.

- When choosing an alternative typeface you need to consider rotation, legibility, and orientation. Sans serif typefaces – those without small projecting extensions at the ends of character strokes – are typically preferred over serif typefaces, due to their minimal flourishes, consistent widths, and generous negative space. Take great care when selecting and using alternative typefaces for Surface; be sure to test legibility on a Surface display before finalizing selections.

  - Evaluate text rendering at all angles before and during application development.

  - Avoid using all capital letters and small capital letters. Sentence case capitalization is more natural, easier to read, and rarely conveys an aggressive tone.

  - If serif fonts are an integral part of a visual brand experience, set them at 30 points or larger for maximum legibility.

  - Typesetting in high-contrast reduces legibility. White text on a black background can create harsh edges and a poor reading experience.

  - Avoid setting text on curved paths.

  - Remember that most Surface objects and controls can be scaled freely. Enforcing minimum scaling limits on objects is sometimes necessary to retain maximum text legibility.

  - There is no substitute for testing font rendering on Surface itself. Make sure to test for legibility, including when text is rotated and scaled.

- Minimum alternative type sizes:

  - 12 points for interface element labels

  - 16 points for body copy

  - 30 points for light typefaces (thin and/or narrow width)

  - 30 points for serif typefaces (containing small projecting extensions at the ends of character strokes)

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- Allow the font size to be adjusted.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-the-font-size-to-be-adjusted/)

#### 5.7.9. Iconography

- Icons can help the Surface experience, but usage must be meaningful.

- Icons as visual hints

  - Icons are useful to visually convey functionality. The function of buttons and other controls is not always obvious to people, and it is not always feasible to use text labels on small controls. In such cases, simple yet bold icons can be used as a supplement to textual button labels. A set of more than 40 sample icons is distributed with the Microsoft Surface 2.0 SDK.

  - Do not use icon buttons when suitable direct touch interactions are available, use icons to hint at functionality. For example, the Surface Launcher is rotatable. Rather than placing a button with a rotate icon in the corner of the Launcher, the Launcher uses subtle rotation arrows to indicate the action people should take.

- Creating custom icons

  - If an icon is needed for your application that is not included in the sample icon set use the following guidelines to develop custom icons:

    - Icons should have simple geometry.

    - Icons should have limited detail.

    - Icons should be scalable.

    - Icons should leverage real world metaphors.

    - Icons should have a similar visual weight.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

#### 5.7.10. Motion Design

- Motion design defines how things move onscreen, a critical part of the Surface experience. Animations always support the content and the experience as a whole. Motion design provides animations and effects that conveys emotion, energy, connection, and responsiveness. They provide visual hints, cues, and an invitation to explore content.

##### 5.7.10.1. Transitions

- Transitions can give context and provide visual hints of where people are in the Surface experience. They help people build mental maps of their experiences, learn how to use controls, and remember where onscreen objects have gone when no longer visible.

- The Surface transition model for shifting between various modes (Attract – Launcher – applications) uses depth to provide navigational context. For example, when you leave Attract to enter Launcher, Attract pushes back in z space – it moves behind Launcher. When you launch an application from the Launcher, the Launcher moves back in z space and pushes Attract back even further. This gives people important context regarding the way they are moving through the experience.

- Develop a transition language or model that is appropriate for the function, character, and style of your application. Consider the type of application that you are developing and create transitions that are fitting and appropriate.

- Transitions that occur in a game may be fun and playful, while transitions that occur in a healthcare application should be brief and succinct. Transitions should:

  - Be seamless

  - Be meaningful

  - Be informative

  - Be application appropriate

  - Be carefully timed. Don’t frustrate people by forcing them to wait through long transitions just to access application content.

  - Provide navigational context

  - Reinforce the application narrative

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

##### 5.7.10.2. Transitions as Visual Hints

- Motion design provides tools that enable people to rapidly learn through observation; without requiring directed tutorials or lengthy demonstrations.

- For example, when the Launcher loads a background container fades in, the application icons slide in, and the application icons compress as they reach the edge of the background container. People see this movement and understand that there are more options than are shown. The sliding movement visually hints that the content is scrollable.

- If the Launcher container suddenly appeared onscreen without any transition, it would seem deceptively static. It would be hard for people to know that the content is scrollable, and that there are more options available than those currently displayed. It is very valuable to use transitions as a way to visually hint at functionality.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

##### 5.7.10.3. Guidance Animations

- Guidance animations teach people how to perform specific touch interactions to accomplish a task. They communicate the way a particular button icon or piece of content should be used and give people feedback to visually explain a task.

- For example, the Access Points use guidance animations to teach people a specific direct touch interaction. When someone touches the static Access Points, a visual indicator and action word animate out of the Access Point. If the person does nothing, the visual indication fades out. If the person slides the Access Point or taps the action word, they navigate to a different part of the Surface experience.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

##### 5.7.10.4. Ambient Animations

- Ambient animations are subtle animations used to indicate that the system is alive, awake, and ready for use. They can help reinforce brand and application personality. Ambient animations are purposefully unassuming and refined using subtle and natural effects.

- Subtle ambient movement in the background can give a Surface experience a lively quality. Use ambient animations in your application to ensure people that the application is responsive and working.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

### 5.8. Playtesting

#### 5.8.1. Range of Abilities / Play Styles

- Players with varying abilities to see, hear, walk, speak and read as well as different heights and body shapes have been included in playtesting.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

#### 5.8.2. Diverse Playtesters

- Players with varying race, ethnicity, gender, sexual orientation and cultures have been included in playtesting.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

### 5.9. Inclusivity

#### 5.9.1. Inclusive representation

- If including human-like characters or culturally-specific objects/references, the game has a true diversity of genders, races, cultures, sexual orientation, and body types and avoids stereotypes or cultural appropriation.

    [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

### 5.10. Text display

#### 5.10.1. Text size

- Console font size should equal or exceed:

  - 26 px at 1080p

  - 52 px at 4K

- PC/VR font size should equal or exceed:

  - 18 px at 1080p

  - 36 px at 4K

- Mobile/Xbox Game Streaming:

  - 18 px at 100 DPI

  - 36 px at 200 DPI

  - 72 px at 400 DPI

  - Scale linearly as DPI increases

    > [!NOTE]
    > Platform-provided screen magnification tools aren't an appropriate mitigation for small text size.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#text-size)

#### 5.10.2. Icon and glyph sizes

- The text contained inside icons and glyphs should also meet the minimum default text size as previously defined for console/PC/VR or mobility/Xbox Game Streaming experiences.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#icons-and-glyph-sizes)

#### 5.10.3. Text scaling

- Players should be able to resize text up to 200%of the minimum font sizes (as previously listed), without the loss of content, functionality, or meaning. As an example, console text at 1080p should be able to be scaled from 26 px to 52 px at 1080p.

  - Large header text should still be visually differentiated from the body when text is scaled.

  - Text that scales beyond the visible screen should have a method to be read (scrolling text, text pop-up windows, or appropriate abbreviations).

  - When text is scaled, the player isn't required to scroll both horizontally and vertically to read text within a single UI. (Scrolling in one direction is OK.)

  - It's acceptable to allow text to be scaled down (made smaller) than the default minimums as previously shown at the user’s discretion.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#text-scaling)

#### 5.10.4. Typefaces and Font styling

- Include at least one sans-serif typeface option.

- If stylistic fonts are used (for example, blood dripping off font), provide a non-stylized font option.

- Ensure that all fonts include complete character sets for all supported languages.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#font-style)

- Use an easily readable default font size.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/use-an-easily-readable-default-font-size/)

- Use simple clear text formatting.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/use-simple-clear-text-formatting/)

#### 5.10.5. Text Spacing

Greater spacing between letters, words, or paragraph lines can increase text clarity, because the reader can more easily identify separations between words. Configurable spacing can also assist players who are using text scaling or larger font sizes.

- For blocks of text that are more than two lines, use the following for when set to the standard font size.

  - Players should have the option to configure their own line width, line spacing, paragraph spacing, letter spacing, or word spacing.

  - If players aren't provided with these configurability options, the minimum suggested guidelines are as follows.

    - Line width: The line width shouldn't be more than 80 characters or glyphs (or 40 if Chinese/Japanese/Korean)—or players can adjust the text to meet this requirement. It should be measured when text is resized to 100 percent and doesn't include spaces in the character count.

    - Line spacing: Line spacing (leading) in blocks of text should be at least a space-and-a-half (1.5) within paragraphs—or players can adjust the text to meet this requirement. Line spacing is measured from the ascender of the first line of text to the ascender of the second line of text.

    - Paragraph spacing: Paragraph spacing is at least 2 times larger than the line spacing—or players can adjust the text to meet this requirement.

    - Letter spacing: The space between letters is at least 0.12 times larger than the font size.

    - Word spacing: The space between words is at least 0.16 times larger than the font size.

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#text-spacing)

#### 5.10.6. Text Case and Alignment

- Font case: Provide the ability to display text in proper sentence case rather than in full caps or full lowercase (if used).

    >[!NOTE]
    >This requirement refers to lines of text. A one- or two-word label is exempt from this guideline.

- Alignment: Text is left/right-aligned based on the player language preference (not centered or fully justified)—or players can adjust the text to meet these guidelines.

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#text-case-and-alignment)

### 5.11. Contrast

- Large-scale text and large-scale visual elements should meet a minimum contrast of 3:1 against their background.

  - On console, large text is defined as:

    - 52 px at 1080p

    - 104 px at 4K

  - On PC/VR, large text is defined as:

    - 36 px at 1080p

    - 72 px at 4K

  - On mobile/Xbox Game Streaming, large text is defined as:

    - 36 px at 100 DPI

    - 72 px at 200 DPI

    - 144 px at 400 DPI

    - Scale linearly as DPI increases

- Standard-sized text and visual elements (those that aren't considered large-scale) that provide important information or context for gameplay should have a contrast ratio of at least 4.5:1 against their background.

- Text on inactive elements should meet a minimum contrast ratio of 3:1 against its background.

  - Inactive elements can include text within symbols, glyphs, or other visual elements that appear within the UI, but cannot be interacted with due to scenarios like:

    - The player has not yet unlocked the game area, item, or option associated with the inactive element.

    - The option or visual element is disabled due to a lack of compatibility between the player’s software or hardware technical specifications and the requirements of the inactive option.

    - Any other scenario in which a visual element present within the UI cannot be interacted with due to circumstances specific to that player.

- Placeholder text, or text entered in an input field should meet a minimum contrast ratio of 4.5:1 (3:1 for large scale text) against the input field’s background.

- A high contrast mode (either light, dark, or both) should be provided. When enabled, the contrast ratios should equal or exceed 7:1 for all UI elements against their background.

>[!NOTE]
> Despite common misconceptions that high contrast modes are intended to increase the separation between light and dark elements, the true intent of high contrast modes include the following: 1) Increase the visibility of important elements. 2) Increase the visual separation between different types of important elements. 3) Increase the visual separation between important elements and unimportant elements

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/102#implementation-guidelines)

- Provide an option to adjust contrast.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-an-option-to-adjust-contrast/)

#### 5.11.1. Contrast Ratio Chart

Text size | Contrast ratio
--- | ---
Standard-size text or visual elements | 4.5 : 1
Large-scale text and visual elements | 3 : 1
Inactive-element text | 3 : 1
High contrast mode elements | 7 : 1
Placeholder or input field text | 4.5 : 1 (standard size); 3 : 1 (large scale)

- When text is displayed over a non-solid color background, the text contrast ratio should be measured between the text and the lowest contrasting area of the background.

- Where available, read the platform-provided contrast settings to determine whether high contrast modes should be turned on/off at game launch by default, and then adjust the game UI accordingly.

- Foreground and background text colors can be configured/set by the player.

- Avoid relying on color alone to communicate information. When this isn't possible, provide players the option to choose the color of key game elements.

- Images shouldn't contain text except for Logotypes.

- Text or visual elements that are part of a logo or brand name have no minimum contrast requirement.

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/102#implementation-guidelines)

### 5.12. Visual and Audio Cues

- Any visual content that's critical to understanding gameplay or comprehending the narrative should be expressed by using at least one other sensory method. As an example, visual gunfire indicators should also be represented by using spatial audio or haptic feedback.

- Game-critical content that's represented through multiple visual affordances (like shape or spatial location) should have an additional means of identification not reliant on vision, such as haptic feedback, spatial audio, or screen narration. Blind and low-vision players might not be able to identify cues that are represented solely by visual means, even if multiple visual methods are used.

- Where menu narration is supported, use images with text alternatives for graphical symbols. Don't use Unicode font glyphs with the desired graphical appearances but with different meanings.

- Any content that's critical to understanding gameplay or comprehending the narrative, and is expressed through color, also needs to be expressed by using at least one additional signifier such as shape, pattern, iconography, or text labels.

- If color is the primary method of communication for information (like if rare items have a blue highlight and legendary items have an orange highlight), the player should be able to configure those colors by using presets, or ideally, free choice of color.

- If a change of color (graying) is used to inform the player of the existence and state of a control that isn't available, another method is also used. (For more detailed guidance about contrast ratios for elements that aren't available, see XAG 102: Contrast).

- Any audio content that's critical to understanding gameplay or comprehending the narrative should be expressed by using at least one other sensory method. As an example, the sound of gunfire should also be represented by using a visual graphic that indicates the type and directionality of the sound. Haptic feedback could also be used.

    >[!NOTE]
    >Not all platforms support input devices with haptic capability (such as mouse/keyboard). Additionally, players with disabilities might be using specialty input devices that don't provide haptic vibration such as the Xbox Adaptive Controller. They might choose to disable haptic vibrations if it causes irritation or pain. Therefore, haptics should be used in addition to other ways of relaying information.

    For more details about the use of haptics in games, see [XAG 110: Haptic feedback](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/110).

- For text-only dialogue that is not accompanied by a spoken audio track, provide the name of the character speaking and an indication of where the speaking character is spatially located in relation to the player’s character.

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/103#implementation-guidelines)

- Use visual hints and guidance animations to teach touch interactions

  - Provide visual hints for unseen content.

    - Intuitive, non-menu driven exploration is fundamental to the Surface experience, and sometimes people require clues and hints to guide them in exploration.

      - For example, the Launcher animation shows application icons scrolling in and then the icons compress to indicate that the Launcher is scrollable and that there is additional content.

  - Provide visual hints that prevent people from doing “wrong” actions.

    - For example, do not allow people to move content outside the bounds of a display where they cannot retrieve it.

  - Use guidance animations to reveal functionality.

    - For example, in a music browsing application, album covers are ScatterView Items, so that people can touch them and flip them over to reveal the contents of the album. When the application is launched, the covers animate into place and a few albums flip over to demonstrate that additional content exists.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

### 5.13. Screen Narration

- All core game UI text (main menu, options, HUD, state changes, players in the game, and time-based events) should support the screen readers that are available on the platform or voice out of the UI through a speech synthesizer. The use of recorded audio files can also be a solution but isn't ideal. (All references to "text" refer to text that can be voiced by using these technologies.)

- Interactable UI elements that behave as lists, tabs, radio buttons, check lists, or combo boxes, must enumerate how many child items belong to that element, the type of input the element requires, as well as the current state or value of that input element. As an example, “Worlds, Tab, 1 of 3, selected,” or “Music Volume, slider, 52%.”

  - Enumeration should occur at the end of a narrated string. For example, "Gama, slider, 38%, 6 of 9."

  - An option to disable enumeration narration can be provided for players who prefer simplified narration.

- The text alternatives for charts, diagrams, pictures, and animations should make the same information available in a form that can be rendered through auditory output. Text alternatives can be used as needed to convey the information in the non-text content.

- Ensure that text alternatives for graphics convey the purpose and operation of the UI components.

- Non-text content that's purely decorative, used only for visual formatting, or isn't presented visually, should not be spoken.

- Support a focus order that's aligned with the meaning or operation of the UI. If the navigation sequence is independent of the meaning or operation, align the focus order with the flow of the visual design.

- After navigating to the last item in the UI/menu structure, the player should be taken back to the first item in the UI/menu structure and vice versa.

    >[!NOTE]
    >This guideline only applies to linear menu structures where focus can be moved either up or down or left or right. Menu structures that allow focus to be moved to elements in any direction (such as a menu with focusable items arranged on a 4x4 tile) don’t need to loop. We encourage developers to have an option to enable and disable menu looping for all menus.

- Players should be able to quickly cancel/repeat narration, regardless of input type (controller, keyboard, mouse, or touch).

- If narration for the current item in focus is actively being read and focus is moved to a different UI element before the narration string has been read in its entirety, the narration for the original UI element should immediately stop, and narration for the new UI element that focus was most recently moved to should begin.

- Allow players to adjust the speaking rate and pitch of the voice used to narrate the UI.

- Context change should be player initiated. After a change in context has occurred, the player should be notified via narration of the new context.

- Players should be notified via narration of events that are relevant to user interactions (changes in component states, value, or description). This includes reoccurring/timed-based notifications such as indications of game state. (For example, loading screens, searching for player notifications, or count-down timers.) In these instances, it's acceptable to read out the state every 7-10 seconds so as not to interfere with other narration/notifications.

- When supporting external screen readers (versus implementing in-game speech synthesis), be sure to do the following:

  - Programmatically expose the language of the game. This means that if the game is in English (for example, the menus are written in English, all text and instructions are in English, or characters speak to one another in English), the game should properly assign the language attribute for English (for example, en-us), and be sure this information is exposed to external software like screen readers. This ensures that the screen reader is announcing information with the proper pronunciations and dialects.

  - If non-player character dialogue involves speaking in a language that differs from the main language attribute assigned to the game, this should also be exposed to the screen reader. For example, a game that has text, menu elements, and majority of character dialogue in English appropriately exposes the game’s language as “English – US” to external screen readers. However, there are a few circumstances in the game where a non-player character (NPC) speaks to their mother, who only speaks Spanish. The dialogue between the character and their mother is in Spanish. In this case, the game should also programmatically expose areas in the game where dialogue or other language differs. This ensures that when a screen reader reads the dialogue text aloud to the player, it also uses the proper pronunciations for the Spanish language.

    >[!NOTE]
    >Proper names, technical terms, words of indeterminate language, and words or phrases that have become part of the vernacular of the immediate surrounding text are exceptions to these guidelines.

  - Example: The game is primarily in English, however phrases like “hors d’oeuvres” or other common phrases that are technically in another language, are part of a fictional language, or are the proper name/technical term for something (for example, Arc de Triomphe du Carrousel) don't need additional programmatic language attributes.

  - When writing alternative text descriptions for images, graphics, icons, or diagrams, don't include the type of object in the description. (For example, if you're writing alternative text for an image of a shield, the alternative text should be “Brown shield” instead of “Image: Brown Shield”).

  - In content that's implemented by using markup languages, elements have complete start and end tags, elements are nested according to their specifications, elements don't contain duplicate attributes, and any IDs are unique. (For detailed articles on using markup languages, see the "Resources and tools" section later in this topic.)

  - For all UI components (including but not limited to form elements, links, and components generated by scripts), the name and role can be programmatically determined. States, properties, and values that can be set by the user can be programmatically set. Notification of changes to these items is available to user agents, including assistive technologies.

- Provide a text alternative that describes any time-based media (like providing an audio description for a video).

- For live content, it's enough if the text alternative provides a descriptive title for the time-based media element. (For example, for a live clock display, the screen reader reads the title as, “Clock displaying current time in Pacific Standard Time Zone,” but doesn't have to repeatedly announce the current time in real time as it changes.)

- Tables should be made fully accessible to screen narration technologies.

  - This is achieved by ensuring that column and row headers are programmatically associated with relevant cells. This supports a player’s ability to derive necessary contexts about the information provided in each individual cell. High level alternative text descriptions for tables should be avoided.

- Provide a mechanism for the player to understand how to pronounce a proper name, technical term, or word of indeterminate language.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/106#implementation-guidelines)

- Ensure screen reader support for mobile devices.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-screenreader-support-for-mobile-devices/)

- Ensure manual / website are provided in a screen reader friendly format.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-manual-website-are-provided-in-a-screenreader-friendly-format/)

- Ensure screen reader support, including menus & installers.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-screenreader-support-including-menus-installers/)

### 5.14. Input

#### 5.14.1. General Input

- Experience enables customizable controls and button mapping.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- UIs throughout the game should support digital and analog navigation, including menu UI and in-game UI.

- A UI should be navigable by using single, non-simultaneous key presses.

- Players should be given the option to remap all of the controls within the game itself, regardless of platform-level remapping support that might be present. This includes remapping analog and digital controls, inverting both the x-axis and y-axis individually for each individual control stick, and the Esc key on PC games.

  - This should ideally allow the player to assign an action to all potential game inputs, as opposed to simply swapping button assignments.

- When a player remaps a control within the game, the labeling of the new mapping is represented correctly across any hints, tips, tutorials, or controller map schemes.

- All interface components should be fully operable with digital input—even if the primary mode of input is intended to be analog. This relates to the function, not the input technique. For example, if a player is using analog triggers for gas in a racing game, the game should work properly if the control is remapped to a digital control like the “A” button.

- Avoid introducing mechanics where a player is required to repeat or execute multiple keystrokes or button presses within a short period of time (like quick-time events (QTEs)).

- Avoid introducing mechanics where a key or button should be held down for an extended period before the input is registered.

- Avoid introducing mechanics where a player is required to press two buttons simultaneously to activate a function.

- If inputs that require repeated button strokes, prolonged button presses, or simultaneous button presses cannot be avoided, provide an alternative input option that is either less physically demanding or allow the player to bypass game events that require the use of these mechanics, or that part of the game experience altogether.

- Ensure that content can be operated without multi-point gestures—or the functionality can also be operated by another method, such as a tap, click, double-tap, double-click, long press (less than 3 seconds), or click and hold.

  - Multi-point gestures are interactions that require two or more points of contact with touch-screen input devices such as mobile phones or tablets. For example, using a “pinch to zoom” gesture or a two or three finger swipe.

- Ensure that content can be operated without path-based gestures. This includes mouse/cursor movements as well as touch-screen, path-based gestures.

  - Path-based gestures usually require a single point of contact. However, these gestures require a certain level of dexterity and coordination to move the cursor in a specific way like swiping horizontally or vertically, clicking and dragging, or drawing specific shapes to initiate the operation.

- For content that can be operated with a single pointer (like a mouse/cursor or touch screen), use the following guidance.

  - The down click or down press (the down event) on an item doesn't automatically activate that item. Activation occurs on the up event, which is when the button or press is being released. (For example, when a player hovers their mouse over a button and clicks, the button’s function is not immediately activated as the player presses their mouse button “down.” The button is only activated on the up event, or as the player is releasing the mouse button. This also applies to touch-screen experiences.)

  - A mechanism is available to cancel the action before completion. (For example, if a player touches down on the wrong location or item, they can move their cursor or finger away from that location before the up event or click release. This cancels the unintended action.)

  - If a mechanism to cancel the action isn't available, a simple mechanism to undo the action is provided.

    >[!NOTE]
    >There might be circumstances where activating the function on the down event is essential. If it's essential, the previous guidelines shouldn't be taken into consideration for that specific function. (Essential down-event functions can include experiences like a simulation of playing the piano or shooting a gun. The experience would become very unnatural if activation didn't occur until the up event).

- Any gameplay-critical input that uses speech or motion controls as a default has an alternative digital input mechanism (for example, a keyboard alternative for a motion-based game).

- Games should not require the use of two analog sticks (or an analog stick and directional pad) to complete mechanics.

  - Some games natively support a single stick due to the style/genre of game. However, even games that traditionally require two sticks (for example, first person shooters) can include options for single stick control.

  - Some games recognize a press-in (or "click") of a stick as an input. Even if the game is not using a second stick for directional input, if a click is required on that second stick, that input should be able to be remapped to another button.

  - Some games use the D-pad for behaviors beyond character movement, such as weapon or item selection. If a game requires using a D-pad for such input, that input should be able to be remapped to other unused buttons or activated through other means other than analog sticks (such as from a menu).

- For games that support keyboard input, players should be able to access all controls needed to start the game, adjust settings, play the game, and exit from the game back to the platform's home screen using a keyboard alone.

- An option to adjust sensitivity of analog controls individually should be provided at the game level. This includes the ability to adjust the sensitivity of analog thumb sticks, joysticks, triggers, racing wheels, and mouse movement as applicable.

  - Players should be able to increase or decrease sensitivity by at least 50% of the default sensitivity.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/107#implementation-guidelines)

- Include an option to adjust the sensitivity of controls.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-an-option-to-adjust-the-sensitivity-of-controls/)

- Support more than one input device.

    [Game Accessibility Guidelines](http://gameaccessibilityguidelines.com/support-more-than-one-input-device)

- Make interactive elements that require accuracy (e.g., cursor/touch controlled menu options) stationary.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/make-interactive-elements-that-require-accuracy-eg-cursortouch-controlled-menu-options-stationary/)

- Ensure that multiple simultaneous actions (e.g., click/drag or swipe) are not required, and included only as a supplementary/alternative input method

    [Game Accessibility Guidelines](http://gameaccessibilityguidelines.com/ensure-that-multiple-simultaneous-actions-eg-clickdrag-or-swipe-are-not-required-and-included-only-as-a-supplementary-alternative-input-method)

- Time-based gestures are problematic.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

- Ensure that all key actions can be carried out by digital controls (e.g., d-pad/pad/keys/presses), with more complex input (e.g., analog, speech, gesture) not required, and included only as supplementary/alternative input methods.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-that-all-key-actions-can-be-carried-out-by-digital-controls-pad-keys-presses-with-more-complex-input-eg-analogue-speech-gesture-not-required-and-included-only-as-supplementary-al/)

- Avoid/provide alternatives to requiring buttons to be held down.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/avoid-provide-alternatives-to-requiring-buttons-to-be-held-down/)

- Do not make precise timing essential to gameplay – offer alternatives, actions that can be carried out while paused, or a skip mechanism.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/do-not-make-precise-timing-essential-to-gameplay-offer-alternatives-actions-that-can-be-carried-out-while-paused-or-a-skip-mechanism/)

- Include a cool-down period (post acceptance delay) of 0.5 seconds between inputs.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-a-cool-down-period-post-acceptance-delay-of-0-5-seconds-between-inputs/)

- Provide very simple control schemes that are compatible with assistive technology devices, such as switch or eye tracking

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-very-simple-control-schemes-that-are-compatible-with-assistive-technology-devices-such-as-switch-or-eye-tracking/)

- Support controllers, such as the [Xbox Adaptive Controller](https://www.xbox.com/en-US/accessories/controllers/xbox-adaptive-controller), and other switch type inputs that allow the user to remap keyboard inputs to control or interact with virtual environments.

    [XR Accessibility User Requirements | XR controller challenges](https://www.w3.org/TR/xaur/#xr-controller-challenges)

- Give users the ability to modify their input preference or use a variety of input devices.

    >[!NOTE]
    >The remapping of keys used to control movement or interaction in virtual environments is not currently required by WCAG. It is nevertheless noted in the literature as desirable.

    [XR Accessibility User Requirements | Customization of control inputs](https://www.w3.org/TR/xaur/#customization-of-control-inputs)

#### 5.14.2. Mobile Input

- Offer players the ability to use non-touch input types such as:

  - Standard controllers

  - Adaptive controllers

  - Physical keyboards

  - Mouse

  - Assistive technologies (platform switch access, voice input, head movement-based controls via the device’s camera, etc.)

- Support mobile-native input accessibility features.

    >[!NOTE]
    >Many mobile platforms like iOS and Android natively support switch access, movement-based controls, and voice controls as described in the following text. 1) Switch control: Players who are unable to interact with their devices directly through touch may be using switch-access buttons mounted near other parts of their body such as their head, arms, or legs to navigate their mobile devices. Ensuring your game is compatible with platform-supported switch access navigation allows these players to use these assistive technologies during their gaming experiences as well. 2) Voice control: Some device platforms support mobile device navigation via voice control. Players may be able to use voice commands to activate inputs or game controls.

- Support gameplay in both portrait and landscape screen orientation.

    >[!NOTE]
    >Some users have their mobile devices mounted in a fixed position onto their wheelchair arm or table. By supporting play in both portrait and landscape orientation, these players can avoid having to change their mounting position or set up.

- Allow players to adjust the size, spacing, and positioning of all touch targets at their discretion.

- Provide a range of pre-set touch target layout configurations.

- The default touch target layout and pre-set layout configuration options should adhere to the following:

  - Touch target areas should be large enough to see and interact with easily. The following are the suggested minimum default sizes:

  - Mobile phones:

    - 15 mm high by 15 mm wide, or 15 mm in diameter
    - 59 by 59 px at 100 DPI
    - 118 by 118 px at 200 DPI
    - 236 by 236 px at 400 DPI
    - Scale linearly as DPI increases

  - Tablets:

    - 24 mm high by 24 mm wide, or 24 mm in diameter
    - 94 by 94 px at 100 DPI
    - 189 by 189 px at 200 DPI
    - 378 by 378 px at 400 DPI
    - Scale linearly as DPI increases

  - Touch targets should be spaced widely enough to prevent accidental activation of other controls.

- Consider surrounding each touch target with a small amount of inactive space to limit accidental activation of other controls.

- Provide players with an opportunity to cancel a decision or correct a recent interaction mistake. For example:

  - Allowing a player to Short Press and Drag to cancel a button press.

  - Allowing a player to undo an action via an “Undo” button.

  - Allowing a player to release a held object or entity by pulling it outside of the playable area.

- Allow players to adjust aspects of input such as swipe sensitivity.

- Consider offering simplified control schemes or options to reduce the number of controls needed to play the game.

- Avoid or provide alternative input options for common challenging input types including:

  - Prolonged touch target holds

  - Dragging or swiping gestures

  - Rapid taps

  - Multi-point gestures

  - Multi-finger gestures or simultaneous button presses

  - Speech input

  - Gyroscopic controls such as tilting or shaking the device

- Control activations should occur on touch-end or mouse-up events.

    >[!NOTE]
    >Touch-end: The control is activated when the user removes their finger from the screen, not the point in which initial contact is made. Mouse-up: The control is activated when the mouse button click is released, not the point in which it is initially clicked downward.

- Support speech-to-text or dictation-based input. This is important for areas like text-based input fields and text-based party chat experiences.

- Ensure the customization process itself is fully accessible. This includes all necessary tasks needed to resize controls, move controls, re-assign controls, or select pre-set layout configurations.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/107#guidelines-for-mobile-input)

#### 5.14.3. Virtual Inputs

- If producing a PC game, support windowed mode for compatibility with overlaid virtual keyboards.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/if-producing-a-pc-game-support-windowed-mode-for-compatibility-with-overlaid-virtual-keyboards/)

#### 5.14.4. Voice Recognition Input

- Experience supports voice recognition inputs.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- Ensure that speech input is not required, and included only as a supplementary / alternative input method.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-that-speech-input-is-not-required-and-included-only-as-a-supplementary-alternative-input-method/)

- Base speech recognition on individual words from a small vocabulary (eg. ‘yes’ ‘no’ ‘open’) instead of long phrases or multi-syllable words

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/base-speech-recognition-on-individual-words-from-a-small-vocabulary-eg-yes-no-open-instead-of-long-phrases-or-multi-syllable-words/)

- Base speech recognition on hitting a volume threshold (eg. 50%) instead of words.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/base-speech-recognition-on-hitting-a-volume-threshold-eg-50-instead-of-words/)

#### 5.14.5. Gaze Control Input

- Experience supports gaze control input.

    [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

### 5.15. Difficulty Options

- Include multiple levels of difficulty presets (ideally four or more, covering a wide range of values to ensure that players with a wide array of gaming experiences and ability levels can choose a difficulty mode that provides the level of challenge that they want).

    >[!NOTE]
    >Game “modes,” such as “creative mode,” aren’t considered a difficulty option if the creative mode doesn’t provide the same gameplay experiences, resources, and opportunities as the primary game mode.

- Provide players with the option to change difficulty at any time without losing game progress, regardless of whether they have already started the game.

- Provide players the ability to regularly save game progress. Ideally, both manual and auto-save options should be provided so that players can continue after failure without significant loss of progress.

- Provide the ability for players to discreetly adjust the difficulty of different mechanics. This can either be through explicit difficulty settings (like Puzzle Difficulty and Combat Difficulty) or through a set of assists (like Brake Assist and Auto-Aim).

- Provide an ultra-low difficulty mode for the game that enables a wide range of players to progress through the narrative.

- Consider providing a mode for players to complete the entire game by using a greatly reduced control scheme. This is important for players with especially severe disabilities or those who simply want to experience the game's narrative.

- Ensure that the language used to describe the difficulty presets is descriptive and doesn't denigrate the player (for example, "Wimp Mode").

- Single player, local multiplayer, and local split-screen games should be pausable at any time (excluding saving/loading screens).

  - Both active game play as well as cinematics (intros, video cutscenes, scripted cutscenes) should be able to be paused at any time.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/108#implementation-guidelines)

- Allow pausing the experience at arbitrary times so people can take breaks.

    [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- Enable users to save progress at any time to avoid the need to repeat challenging actions or simply to allow them to pick up where they left off in the experience.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

### 5.16. Objective Clarity

- Provide players with the ability to review tasks and objectives at any given time. Descriptions of tasks and objectives should be clear and straightforward.

- Include a log-style list of all the objectives and tasks that a player has completed to date.

- Provide options to enable waypoint or path markers, hints, or other reminders and directional cues for players when it appears that they've made no progress after a period of time (this varies by game/genre). These options could be included in difficulty presets.

- Provide the player a clear description of any progress made toward meeting prerequisites to progress through the game (for example, “15/20 skulls collected" or "3 of 5 hidden switches found”).

- Interruptions (like notifications or side quests) that aren't directly related to the objective at hand can be postponed or suppressed by the player.

- Provide the ability to revisit the game’s narrative (for example, the ability to replay cutscenes or view a written summary of the story thus far).

- Saved files should be descriptive. Ideally, they should contain a screenshot, a time stamp, and a brief summary of the player's current progress and objectives.

- Gameplay tutorials that explain or demonstrate core game mechanics should be made available for players.

  - Tutorials should be interactive, such as having the player carry out the game mechanics and controls being taught in the tutorial in a simulated or real gameplay environment or be provided in the form of video demonstrating the mechanics and controls for players to passively watch.

  - Static screens that display game controls or controller mappings are not sufficient and should not be considered a tutorial.

  - Tutorials should be available on-demand for players to access at any point in the game. For example, a tutorial may be a level within the game, or its own separate experience from primary gameplay, but players should be able to revisit the tutorial at any point in the game, regardless of whether the tutorial has previously been completed.

  - Players should be provided an option to enable subtitles for tutorials with voiceover, character narration, or dialogue.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/109#implementation-guidelines)

- Integrate learning with doing

  - If interaction instructions are necessary, integrate them with the flow of the application, do not divert focus away from content.

  - Make essential features immediately discoverable.

    [Microsoft Surface 2.0 Design and Interaction Guide](http://microsoft.com)

### 5.17. Audio Description

- All media content that was broadcast previously with audio descriptions on television and that appears in a game or on the title’s website should be audio described.

  - Example: A game shows a 30-second video clip from a television show in one of its cutscenes. When this clip originally aired on television, audio descriptions were included in the broadcast. As a result, the game that was using this television clip as a cutscene should also provide audio descriptions for this clip when it appears in the game.

- Appropriately localized audio descriptions should be available for FMVs or in-game scripted cinematic events, if the player wants to enable them.

  - These descriptions should play during natural gaps during video playback. In cases where natural gaps are insufficient to allow audio descriptions to convey the sense of the video, extended audio descriptions can be provided. This temporarily pauses the video or scripted event to allow enough time for each segment of audio description to play out.

- If the game doesn't offer audio descriptions, consider providing full transcripts of all FMVs or in-game scripted cinematic events via an accessible website or other accessible format that includes important visual content, such as facial expressions of characters, narratively important actions, non-speech sounds, and dialogue.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/111#implementation-guidelines)

### 5.18. Error Messages and Destructive Actions

- If an input error is automatically detected, such as incorrectly entering a password, the error and the method to correct the error is described to the player in multiple ways (like through text or voice narration).

    >[!NOTE]
    >Providing information that would jeopardize the security or purpose of the content is exempt from this guideline.

- Make error and warning messages easy to visually distinguish from other text on the screen.

- Visually emphasize errors and warnings where they've occurred.

- If any action the player takes will result in stored data that they control being deleted or modified in any way, provide the player an opportunity to review and correct the data or completely reverse the action before committing it.

- Offer players a mechanism to review, confirm, and undo permanent or destructive actions (for example, making an in-game purchase, selling an item, or overwriting a game save).

- Don't require button holds for confirmation of destructive actions. Provide alternate options to button holds in these scenarios.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/115#implementation-guidelines)

### 5.19. Time Limits

- When time limits are imposed for any UI interaction (not related to core game mechanics):

  - Time limits are used only when they're essential and unavoidable.

  - The player is informed (in multiple ways) when they're about to encounter a time limit.

  - There's a method to modify the time limit. The player can:

    - Request a longer session time limit, or no time limit for the session before the time limit begins.

    - Adjust the time limit before encountering it, up to at least ten times the length of the default limit.

    - Be warned before time expires and be given at least 20 seconds to extend the time limit with a simple action (for example, "press the A button"), and the player can extend the time limit at least ten times.

    - Turn off the time limit.

- When imposing time limits that control the duration that an important element appears on screen (for example, the amount of seconds a tutorial text window, speaker dialogue, or text-chat/speech-to-text communication window remains visible):

  - The player is able to adjust the number of seconds that these elements appear on screen before encountering them (such as in a settings menu), up to at least ten times the length of the default limit.

  - Alternatively, the player can disable duration limits. Elements can be dismissed or advanced to the next tutorial window or dialogue text on input.

- Exception: A time limit imposed by the content is exempt from this expectation if at least one of the following is true.

  - The time limit is a required part of a real-time event (for example, an auction), and no alternative to the time limit is possible.

  - The time limit is essential to the task.

  - The default time limit exceeds 20 hours.

    >[!NOTE]
    >Real-time multiplayer events, such as countdown timers in a lobby, aren't required to provide an ability to extend or adjust the amount of time until gameplay will start because this would affect the play of other players in the matchmaking session.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/116#implementation-guidelines)

### 5.20. Visual Distractions and Motion Settings

- When moving, blinking, scrolling, or auto-updating content is presented on a UI screen that also contains text, provide players with the following:

  - Auto-updating content:

    - A method to control the frequency of updates to on screen content.

    - A method to pause, stop, or hide auto-updating content.

  - Moving, blinking, scrolling, or flashing content:

    - A mechanism to entirely disable this content.

    - A mechanism to pause or hide this content.

>[!NOTE]
> Ancillary gameplay that occurs surrounding the text-based UI experience isn't subject to this.

- Avoid the use of camera shake, camera bobbing effects, motion blur, mouse blur, and more or provide an option to turn off these behaviors.

- Avoid any repetitive side-to-side or up-and-down on-screen movement, except that which is core to game play. This includes behaviors such as "weapon sway" or "camera bobbing."

- Provide adjustable field of view settings.

>[!NOTE]
>This allows players to choose a field of view or angle that is least likely to make them sick based on their sitting distance from their screen and other factors.

- Provide camera movement settings like the ability to adjust horizontal and vertical camera movement sensitivity and the ability to disable automatic camera movement.

- Allow players to choose between 1st and 3rd person camera views.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117#implementation-guidelines)

### 5.21. Photosensitivity

- Games shouldn't include images/experiences that might cause adverse reactions, such as seizures or migraine episodes, during gameplay.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118#implementation-guidelines)

#### 5.21.1. Luminance flash failure

- Definition:

  - A flash is defined as a 10% change in luminance (where 100% is the maximum luminance of a white screen)

  - The darker luminance value should be below 0.8.

- Failure criteria:

  - Flashes occur too frequently (approximately more than three per second).

  - Flashes take up a certain amount of the screen (approximately 20 percent or more).

  - Lower intensity flashing can also cause a failure if it's continued for an extended period of time.

- How to address:

  - Reduce the contrast between the brightest and darkest parts of the flash.

  - Reduce the frequency of the flashing.

  - Decrease the size of the flashing.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118#implementation-guidelines)

#### 5.21.2. Red flash failure

- Definition:

  - A red flash requires a lower change in luminance than a normal flash.  Specifically, it applies when either extreme of the flash is a saturated red (R/(R + G + B) >= 0.8).

  - A flash here is defined when the change in the value of (R-G-B) × 320 is greater than 20.

- Failure criteria:

  - Flashes occur too frequently (approximately more than three per second).

  - Flashes take up a certain amount of the screen (approximately 20 percent or more).

  - Lower intensity flashing can also cause a failure if it's continued for an extended period of time.

- How to address:

  - Desaturate the red coloring.

  - Reduce the contrast between the brightest and darkest parts of the flash.

  - Reduce the frequency of the flashing.

  - Decrease the size of the flashing.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118#implementation-guidelines)

#### 5.21.3. Spatial pattern failure

- Definition:

  - Alternating bands that have high contrast define a spatial pattern.

- Failure criteria:

  - The difference in contrast is greater than 10 percent.

  - The pattern takes up a large part of the screen (approximately 20 percent or more).

- How to address:

  - Reduce the contrast between the bands.

  - Decrease the size of the pattern.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118#implementation-guidelines)

### 5.22. Speech-to-Text (STS) & Text-to-Speech (TTS) Chat

- Speech-to-text chat: Players can enable speech-to-text chat to have all voice-based communication from other players transcribed into text in real time.

- Text-to-speech chat: Players can enable text-to-speech chat. When enabled, players are provided a text-entry box. All outgoing text that the player enters into the text-entry box is transformed into synthesized audio in real time and broadcast on the voice channel to all other players.

- Text-entry box: A text-entry box should be made available for players to enter text everywhere communication is available.

- Screen narration (text-based communication): All incoming text-based communications from other players should be voiced out in real time locally to a player with screen-narration settings enabled.

- Screen narration (non-text communication): All phrases, emojis, or emotes should be voiced out in real time locally to a player with screen-narration settings enabled.

  - Emojis should be voiced out with friendly names, such as “Grinning Face” or “Two Hearts,” based on the CLDR Short Names provided by Unicode.org.

- Player-initiated character voice: All player-initiated character communication spoken aloud that conveys intent to another player, such as the audio voice-over of a predefined message from a chat wheel, should be transcribed into text, in real time, and displayed locally to a player with speech-to-text chat enabled.

- It's also important to note that the process of reviewing predefined message options is also accessible. Players with screen narration enabled should be able to hear a preview of each message aloud when it receives focus so that players know what they're selecting before sending it.

- Read and support platform settings: Games should, by default, support platform settings that enable speech-to-text chat or text-to-speech chat where those settings exist.

- Provide in-game platform setting overrides: Games should ensure that all core supported features (speech-to-text chat, text-to-speech chat, and screen narration) can be adjusted at the game level. For example, a player has text-to-speech chat enabled at the platform level, and they can disable text-to-speech chat at the game level through a designated menu item in the game’s settings UI.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/119#implementation-guidelines)

- Developers should include optical character recognition (OCR) as a feature of text-to-speech (TTS) so that words included in images may be deciphered by low vision users.

- In addition to Text-to-Speech (TTS), audio augmentation elements should include labeling objects or elements and allowing users to have those objects audibly identified as they encounter or explore those objects in the platform or app.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- Realtime text <-> speech transcription.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/realtime-text-speech-transcription/)

### 5.23. Communication Experiences

- If a game offers one-to-one or one-to-many communication experiences (like voice chat, text chat, or any other method of connecting players so that they can communicate with one another), it's especially important that the following scenarios be accessible in accordance with all relevant XAGs.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/120#implementation-guidelines)

#### 5.23.1. Navigating to communication features

- The necessary UI path for accessing, launching, or using communication features should be accessible:

- If a player must navigate through the main menu to turn on communications, the selection, launching UI, and any other subsequent menus on the path to communicating with other players should be usable by a player with a disability.

  - Example: A player must navigate through the main menu to get to the multiplayer screen where they can begin the matchmaking process. After the player has been connected to a lobby, the game loads and then launches into the multiplayer match. In the match, players can begin using communication features. In this example, the experience from the main menu to the match falls under the scope of these requirements. This includes navigating the multiplayer screen to choose a specific type of match, subsequent pathways such as adding players to the game, the loading screen between matchmaking and gameplay, and the point in the game where communication features can be launched and used.

- If a player must select or create a character, join a server, or take some other action to reach the experience that uses communication features, the UI for navigating these selections should be accessible.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/120#navigating-to-communication-features)

#### 5.23.2. Configuring the Communication Experience

- All of the necessary UI for enabling or managing settings that affect communication features should be accessible. Consider the following examples:

  - The necessary menus for enabling any communication-related accessibility settings, such as the following, should be usable by a player with a disability.

    - Turning text-to-speech chat and speech-to-text chat on or off; adjusting screen brightness and contrast.

  - The necessary menus for changing audio or other settings that affect the communication experience, such as the following, should be usable by a player with a disability.

    - Volume settings for player chat, text-to-speech chat, ambient volume, and music.

  - The necessary menus or settings for managing communications-related notifications, such as the following, should be usable by a player with a disability.

    - The ability to adjust how long notifications appear on screen.

    - The ability to turn certain notifications on or off.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/120#configuring-the-communication-experience)

#### 5.23.3. Using Communication Features

- All of the necessary UI for meaningful participation in communications should be usable by a player with a disability. Consider the following examples:

  - Sending and accepting friend requests.

  - Searching for friends and other players.

  - Actions and status of other players, such as muting, online or offline status, current availability, and blocking.

  - Opening and closing chat windows, focusing on and using chat window features, selecting and sending predefined messages in chat wheels, reporting abuse, and any other steps to send communications.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/120#using-communication-features)

### 5.24. Accessible Feature Documentation

- All game-related accessibility features, functionality, user guides, and product support options should be described in accessible, easy-to-discover online product documentation.

  - For websites, this means adherence to [Web Content Accessibility Guidelines (WCAG) 2 Level AA Conformance](https://www.w3.org/WAI/WCAG2AA-Conformance).

  - Each game title should have its own designated web page for accessibility information to provide players with a simplistic and easy-to-consume experience. Using a single web page for accessibility information on multiple titles should be avoided.

- All product documentation that's related to accessibility should be localized into relevant local languages. If the game is localized in other languages, accessibility documentation should also be available in the same languages.

- When in-game Help systems are present, all accessibility features and functionality should be explained in an accessible format.

- Accessibility documentation, regardless of location (such as on a website or in-game), should use up-to-date and respectful terminology for people with disabilities.

  - While global differences do exist, generally speaking person-first language (for example, "gamers with disabilities") is recommended over disability first language (for example, "disabled gamers").

  - Terminology such as "handicapped," "impaired," and "incapacitated" are all examples of antiquated language that is no longer used and may be offensive. Style guides, such as the one provided by the [National Center on Disability and Journalism](https://ncdj.org/style-guide/), can be useful references when crafting documentation.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/121#implementation-guidelines)

### 5.25. Accessible Customer Support

- At no extra cost, players and individuals with disabilities should be able to access call centers and customer support regarding the product in general and the accessibility features of the product.

- Multiple accessible methods should be made available to contact support, including phone, TTY, email, and chat.

    [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/122#implementation-guidelines)

### 5.26. Mental Health Best Practices

>[!NOTE]
>The guidelines in this XAG are applicable to games containing content that may cause adverse emotional or psychological responses including (but not limited to) the types of content listed below: 1) Depictions of events or scenarios commonly related to post-traumatic stress disorder and other mental health conditions such as military combat, physical or sexual assault, domestic violence, violence against animals and children, death of a loved one, discrimination (hate crimes, racially motivated murders, bullying), corrupt or oppressive governments, cults, and more. 2) Sources of common phobias (spiders, snakes, clowns, injections and needles, heights, water/drowning, and more). 3) Portrayal of commonly known addictive substances and behaviors such as alcohol consumption, drug use, simulated or virtual gambling mechanics, and more. 4) Depictions or allusions to behaviors like self-harm, suicide, binge eating, purging, restricting food intake, abuse of drugs or alcohol, and more. 5) Depictions or interpretations of game characters with mental health conditions including depression, post-traumatic stress disorder, psychotic conditions, obsessive-compulsive disorders, anxiety, eating disorders and more.

- Provide detailed descriptions of game content that may cause adverse emotional or psychological responses for players.

  - These descriptions should be available via free online documentation that players can review prior to purchasing the game in addition to appearing within the game itself

    >[!NOTE]
    >Any online documentation regarding content warnings or descriptions should be fully accessible to players by adhering to web accessibility standards.

- Provide warnings upon game launch that inform players of content that may cause adverse emotional or psychological responses.

- Provide an option that allows players to enable in-game warnings prior to entering game areas, cutscenes, or character dialogues containing content that may cause adverse emotional or psychological responses for players.

- When applicable, provide players with customization options that lessen or remove the presence of potentially harmful content.

  - This includes options to customize the visual appearance of content or characters as well as options to remove or limit elements like gore, profanity, animal killing, etc.

    >[!NOTE]
    >This provides players an option to experience the rest of the storyline and mechanics of your game without having to experience content that may cause them adverse reactions or psychological responses.

- Provide players an option to skip cutscenes or missions that deal with particularly psychologically or emotionally challenging content.

- Provide resources in-game to support players with mental health conditions or learn more about mental health. This can include regional helplines, websites with mental health resources, and more.

- Ensure all content warnings and related settings are fully accessible. While meeting these guidelines, make sure to follow other guidelines that intersect, such as XAG 101: Text display, XAG 102: Contrast, XAG 106: Screen narration, and XAG 116: Time limits.

- Ensure characters with mental health conditions are portrayed in an accurate and respectful light that avoids stigmatized or stereotyped behaviors and actions including (but not limited to) the following:

  - Portraying characters with mental illnesses or psychiatric disabilities as consistently unpredictable, extremely violent, or void of reality.

  - Simplifying the experience of those with conditions like obsessive-compulsive disorder down to solely someone who performs repetitive, ritualistic behaviors.

  - Portraying characters with learning or cognitive disabilities as “child-like” and infantilizing their experiences.

  - Associating mental illness with villainy – suggesting that all people with mental illnesses are to be feared and may abuse others or that mental illness is the sole cause of villainy.

    >[!NOTE]
    >It is important to work with the disability community to ensure that all disabilities are represented in an accurate and non-stigmatizing manner

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/123#implementation-guidelines)

### 5.27. Multiuser

- Create experiences for several people to use at the same time.

- Make sure everyone can reach and use key application elements from all sides of the unit.

- Understand how people share screen space

  - Applications designed for many people to use at the same time need to make it easy for more than one person to see, reach, and touch content.

    - Make it clear to everyone when an important application-wide change occurs.

    - Make sure one person's touch interactions don't unexpectedly affect other people's experience.

      - For example, it's problematic in a paint application if one person selects an eraser control and causes everyone's touches to unexpectedly start erasing content.

  - Enable people to move and share controls; do not attach shared controls to one side of the display.

  - Communicate content possession through placement; if new content belongs to a particular person, place it in front of them on the screen. If the group shares a piece of content, place it in the center.

- Support different levels of collaboration

  - There are three distinct levels of collaboration::

    - Highly collaborative: People help each other with the same task to accomplish a shared goal.

    - Somewhat collaborative: People work on separate tasks in order to accomplish a shared goal; also known as "divide and conquer".

    - Non-collaborative: People engage in separate tasks to accomplish different goals.

  - Understand how to best support different levels of collaboration within your application.

    - Enable several people to simultaneously use content and controls.

      - Do not block progress by requiring everyone to use a common set of controls; allow people to break up portions of the task by physically dividing up and sharing the controls.

    - Do not segment the screen into areas tied to particular functions.

      - It is problematic when applications designate one side of the display to perform a specific task, and the other side of the screen to perform another.

- Understand how people share Surface applications.

  - Surface is optimized for many people to use at the same time, but applications should also be designed for use by a single person. Individuals can use applications and encourage others to join them to share the experience.

    - Ensure the number of people using an application doesn't affect its functionality.

      - Enable a single person to enjoy the experience without requiring other people to participate.

      - Enable new people to join without disrupting the experience for people already using the application.

      - Make sure your application can continue with fewer people, allowing a person to leave without disrupting all others' experience.

    - Create experiences that come alive with several people so that the experience is more fun or efficient when people share simultaneously.

    - If appropriate, your application might enable people to divide up their tasks and decide for themselves whether they will be engaged in a collaborative experience or just share the screen to achieve separate goals.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- Support voice chat as well as text for multiplayer games.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/support-voice-chat-as-well-as-text-for-multiplayer-games/)

- Support text chat as well as voice for multiplayer.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/support-text-chat-as-well-as-voice-for-multiplayer/)

- Provide visual means of communicating in multiplayer.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/support-visual-means-of-communicating-in-multiplayer/)

- Allow a preference to be set for playing online multiplayer with players who will only play with or are willing to play with voice chat.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-a-preference-to-be-set-for-playing-online-multiplayer-with-players-who-will-only-play-with-are-willing-to-play-without-voice-chat/)

- Allow a preference to be set for playing online multiplayer with/without others who are using accessibility features that could give a competitive advantage

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-a-preference-to-be-set-for-playing-online-multiplayer-withwithout-others-who-are-using-accessibility-features-that-could-give-a-competitive-advantage/)

### 5.28. Physical Objects

- Use physical objects to enhance the experience.

- People will immerse themselves in Surface experiences, ensure this remains uninterrupted by merging the physical and virtual worlds.

- Use tagged objects.

  - A key differentiator for Surface is its ability to recognize physical objects. Objects help to connect people to the application experience in a tangible way that is not possible with traditional user interfaces.

  - Placing special tags on an object can help the system quickly and correctly identify it. A tag is a unique pattern of dots that consists of a geometric arrangement of infrared reflective and absorbing areas. When a tagged object is placed on the screen, the vision system reads the tag and determines its value, location, and orientation.

    - Use objects to enhance the way people share and own space.

      - For example, an education application might use objects assigned to each student to track lesson progress.

    - Use objects to enable playful, delightful experiences.

      - For example, game pieces may have various animations assigned to different pieces. When a player places the game piece on the screen, the tag triggers an animation to play.

    - Use objects to create a physical link between people and their content.

  - Applications that utilize tagged objects should:

    - Respond immediately to tagged objects. This immediate response lets people know that the device is working.

    - Create a visual response that is appropriate for the object.

    - Clearly connect the physical objects with their virtual effects.

  - Use objects to enhance and enrich the experience, but don’t require the presence of tagged objects.

  - Use non-infrared reflective objects for tagging, so that the reflective portions of the object do not generate contacts within your application.

  - If infrared-reflective objects are required, use your knowledge of the tag location and shape of the object to filter (ignore) these contacts.

- Use untagged objects.

  - An untagged object is referred to as a blob. Surface can detect IR-reflective objects that are placed on the screen. Contacts from untagged objects are the same as contacts from other objects that register as blobs, such as an entire hand placed down on the Surface screen.

  - Applications that utilize untagged objects should:

    - Respond immediately to the presence of untagged objects. This immediate response lets people know that the device is working.

    - Always give a visual indicator when an object is placed on the screen showing that Surface can see it, even if it cannot specifically identify it.

    - Do not rely on blob properties to determine the precise shape or size of physical objects. The shape of all objects on Surface is elliptical, and the size denotes only the IR-reflective portions of objects.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

### 5.29. Product Marketing Requirements

- Provide details of accessibility features on packaging and/or website.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-details-of-accessibility-features-on-packaging-andor-website/)

- Provide details of accessibility features in-game.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/provide-details-of-accessibility-features-in-game/)

## 6. Accessible Process Requirements

### 6.1. Solicit Feedback

- Solicit accessibility feedback.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/solicit-accessibility-feedback/)

### 6.2. Testing

- Ensure the interface is truly accessible from all sides of the Surface unit. Start using and testing the application in various orientations from the start of application development. Make sure many people share the application at the same time throughout the testing process.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- Include some people with impairments amongst play-testing participants.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-some-people-with-impairments-amongst-play-testing-participants/)

- Include every relevant category of impairment (motor, cognitive etc) amongst play-testing participants, in representative numbers based on age / demographic of target audience.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/include-every-relevant-category-of-impairment-motor-cognitive-etc-amongst-play-testing-participants-in-representative-numbers-based-on-age-demographic-of-target-audience/)

### 6.3. Sound Design

Sound design for Surface should draw heavily from the Surface design principles. Adhere to the following guidelines when developing or using sounds for Surface applications.

1. Make sounds simple and subtle

1. Ensure sounds are authentically digital

1. Use sound judiciously. Sound is often difficult to hear in public locations. If sounds are overbearing or annoying people will mute the speakers or remove the application.

1. Make sure all application sounds are at a level (volume) consistent with the sounds in the Surface Shell and Launcher. If sounds suddenly spike in the middle of an experience people will mute the speakers or remove the application.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

### 6.4. Language and Text Design

- Surface experiences typically require little interface text, but this will vary with the type of application you are developing. Text should be content oriented and used judiciously.

- Using the Surface design principles to influence the personality, terminology, capitalization, and punctuation of text will add an extra layer of polish to applications and significantly enhance usability.

- Personality and disposition: The personality of text in Surface applications should be lively, clear, and consistent. It should not include soulless, jargon filled, incomprehensible computer-like language that prevents people from enjoying themselves – or asks them nonsensical questions in cryptic dialogue boxes. The disposition of text in Surface applications should be friendly, lighthearted, and empathetic. Application text should not be rigid, snobby, or uninformative. An easy way to see if the text in your application has the right personality and disposition is to see if it sounds like a friend assisting another friend with a task or objective. For example a message like “Error Code: C82FF4B696” or “Critical data not found” is likely to confuse, frustrate and even anger people. A message with the right personality and disposition might look something more like, “There is some info missing here. Please put your name in the text box to continue.”

- Capitalization: Surface displays text in lowercase and all caps layouts in many places, but also uses title caps, where the first and last words of the phrase and all words in between are capitalized, and sentence caps where only the first word of a sentence is capitalized. Title caps exceptions are articles (a, an, the), coordinating conjunctions (and, but, for, not, or, so, yet), and prepositions with four or fewer letters (at, for, in, into). For example, “Neon Tetras in My Fish Tank.” Sentence caps exceptions are words that are normally capitalized in text such as proper nouns or feature names. For example, “I want to visit Mt. Rainier in the springtime.”

- Maintain consistent capitalization practices to prevent disjointed or jagged reading experiences.

  - Use lowercase for:

    - Content titles

    - List titles

    - List items

    - Interface control labels

    - Example text that appears in search and text boxes

  - Use sentence caps for

    - Checkbox and radio buttons labels

    - Progress indicators

    - Status, notification, and explanatory text

    - Toggle switches

  - Use all caps for:

    - Application titles

    - Dates and times

    - AM or PM

- Punctuation

- Use consistent punctuation to avoid confusion, clarify ambiguous text, and provide direct emphasis as needed.

  - Ampersand ( & )

    - Okay to use in settings or menu lists, for example: Date & Time; Clocks & Alarms.

  - Colon ( : )

    - Do not use a colon at the end of labels for controls such as text boxes, drop-down menus, and progress bars.

    - Do not use a colon when the text box or drop-down list is embedded in a sentence or when the drop-down list appears in the main window.

    - Do not use a colon at the end of group headings or column headings.

    - Use a colon to introduce numbers or other variables, for example: Percent Downloaded: XX%

  - Ellipsis ( … )

    - Use an ellipsis in progress indicator labels to indicate a continuing action, for example, when a person downloads a file. Even if there is a visual progress indicator, you still want to use the ellipsis.

    - Do not use an ellipsis in headings.

    - Do not use an ellipsis in button labels.

  - End punctuation ( . ? ! )

    - Use end punctuation only in instructional text. Do not use end punctuation if instructional text appears in a label or button.

    - Do not use a period at the end of option or check box text labels, even if the label is a sentence.

    - Separate sentences with one space after the ending punctuation, not with two spaces.

    - End a question with a question mark. Avoid phrasing labels as questions.

  - Parentheses ( )

    - Avoid using parentheses in applications if possible, but use parentheses if you need to include an acronym or other short piece of information.

    [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

## 7. Accessible Technology Platform Requirements & Responsibilities

### 7.1. Setup

- Device setup and out of box experience should be fully accessible.

- Device setup should not require the use of a secondary device (e.g, phone, PC, tablet). If it does, the secondary device must be able to be set up in an accessible way.

- Devices should not require the use of companion apps for setup or basic functionality.

  - The inability to access a companion app should not deprecate the basic functions of the device or "brick" it.

- Companion apps must be accessible.

- Devices should not require a persistent internet connection to provide basic functionality and should provide a great and resilient offline experience.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

## 8. Accessible Software Library Requirements & Responsibilities

- Libraries like Three.js, A-Frame, etc.

## 9. Accessible Platform Requirements & Responsibilities

### 9.1. Developer Tools

- Platform developer tools must be accessible.

    [James Maki | Inclusive Reality](http://inclusivereality.com)

### 9.2. Accessibility Test Tools

- Accessibility testing tools must be able to evaluate 3D scenes in addition to 2D UI.

    [James Maki | Inclusive Reality](http://inclusivereality.com)

### 9.3. Platform Privacy

- Accessibility must not come at the cost of privacy. Users must not have to choose between privacy and accessibility. All user interactions must be private by default. Users must opt-in to share interaction data with any entities. If an experience doesn't support full privacy, it's not accessible.

- User interaction data must not enable user fingerprinting.

- Interactions must not require the use of personally identifiable information.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

### 9.4. Platform Security

- Accessibility must not come at the cost of security. Platforms and devices must be secure and prevent the intentional or unintentional sharing of private data and user interactions with any entities. If a platform or device is not secure, then it's not accessible.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

### 9.5. Platform Save Settings

- Allow settings to be saved to different profiles, at the platform level.

    [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/allow-settings-to-be-saved-to-different-profiles-at-either-game-or-platform-level/)

### 9.6. Platform Visual

#### 9.6.1. Platform Contrast Preference

- Platform must provide indication to the application for high/low contrast mode.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

#### 9.6.2. Platform Light / Dark Mode Preference

- Platform must provide indication to the application for light mode / dark mode preference.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

#### 9.6.3. Platform Background Detail Preference

- Platform must provide indication to application for the removal or reduction of background details.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

### 9.7. Platform Audio

- Platforms should provide the option to switch between spatial, stereo, and monaural audio.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

#### 9.7.1. Platform Background Audio

- Platform must provide indication to application for the removal or reduction of background audio elements.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

### 9.8. Platform Pause

- Platforms should enable developers to enable users to save progress at any time to avoid the need to repeat challenging actions or simply to allow them to pick up where they left off in the experience.

    [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

### 9.9. Speech Synthesis

- Platforms should enable developers to consistently enable Speech-to-Text (STT) and Text-to-Speech (TTS)

    [James Maki | Inclusive Reality](https://inclusivereality.com)

### 9.10. Platform Subtitle and Closed Captions

- Platform should support the following subtitle and caption formats:

  - SRT

    [James Maki | Inclusive Reality](https://inclusivereality.com)

### 9.11. Platform Typefaces

#### 9.11.1. Platform Supported Typeface Requirements

- Accessible typefaces should include support for the full unicode character set.

- Accessible typefaces should include support for the following font weights:

  - 100 Thin / Hairline

  - 200 ExtraLight

  - 300 Light

  - 400 Normal / Regular / Book

  - 500 Medium

  - 600 SemiBold / DemiBold

  - 700 Bold

  - 800 ExtraBold / Ultrabold

  - 900 Black / Heavy

- Typefaces should generally be displayed at a font weight of 600 (SemiBold / DemiBold) or greater.

- Typeface should be designed to be read at all viewing angles and rotations to enable 360° x 360° readability.

- Typeface characters must be visually distinguishable from one another. For example:

  - A lowercase `l` character must be visually distinct from a capital `I` character and a number `1` character.

  - A lowercase `q` character must be visually distinct from a lower case `b` that is rotated (in this case 180°) from its normal orientation.

- Typeface tracking should provide ample space to provide clear legibility at small sizes or greater distances.

- Typeface counters (the enclosed areas in letters like `a` and `e`) should be open enough to retain their readability at small sizes or greater distances.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

### 9.12. Input Remapping

- Platform should enable remapping of inputs to alternate controllers, sensors, keyboards, and human interface devices (HID).

    [James Maki | Inclusive Reality](https://inclusivereality.com)

### 9.13. Tab-based Navigation

- Platform should enable tab-based navigation to seamlessly enable navigation between 2D and 3D interactable elements.

  - For example a user should be able to tab between 2D UI elements and continue tabbing through 3D user interface elements.

    [James Maki | Inclusive Reality](https://inclusivereality.com)

## 10. Accessible Development Environment and Tools Environment Requirements

[To be added.]

## 11. Accessible Technology Requirements

### 11.1. Access to Broadband

- High speed internet

### 11.2. Access to Devices

- Hardware devices

- Assistive technology devices

## 12. People Categories

Categories | -
--- | ---
People with low vision | -
People with little or no color perception | -
People without hearing | -
People with limited hearing | -
People with cognitive disabilities | -
People with learning disabilities | -
People who are reading text on a small screen, sitting far away from the screen, on a screen with glare, or on a low-contrast display | -

[Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101#potential-player-impact)

## 13. Glossary

### 13.1. Monaural / Monophonic / Mono Audio

### 13.2. Stereophonic / Stereo Audio

### 13.3. Binaural Audio

### 13.4. Surround Sound

### 13.5. Spatial Audio

### 13.6. Monoscopic Video

### 13.7. Stereoscopic / Stereoscopy Video

### 13.8. Two-dimensional (2D)

### 13.9. Two-point-five dimensional (2.5D)

### 13.10. Three-dimensional (3D)

### 13.11. Extended Reality (XR)

As with the [WebXR API spec](https://immersive-web.github.io/webxr/) and as indicated in the related [WebXR explainer](https://github.com/immersive-web/webxr/blob/master/explainer.md#what-is-webxr), this document uses the acronym XR to refer to the spectrum of hardware, applications, and techniques used for virtual reality or immersive environments, augmented or mixed reality and other related technologies. Examples include, but are not limited to:

- Immersive or augmented environments used for education, gaming, multimedia, 360° content and other applications.

- Head mounted displays, whether they are opaque, transparent, or utilize video passthrough.

- Mobile devices with positional tracking.

- Fixed displays with head tracking capabilities.

The important commonality between them being that they all offer some degree of spatial tracking with which to simulate a view of virtual content as well as navigation and interaction with the objects within these environments.

Terms like "XR Device", "XR Application", etc. are generally understood to apply to any of the above. Portions of this document that only apply to a subset of these devices will be indicated as appropriate.

[XR Accessibility User Requirements | What does the term "XR" Mean?](https://www.w3.org/TR/xaur/#what-does-the-term-xr-mean)

### 13.12. Virtual Reality (VR)

Virtual reality and immersive environment definitions vary but converge on the notion of immersive computer-mediated experiences. They involve interaction with objects, people and environments using a range of controls. These experiences are often multi-sensory and may be used for educational, therapeutic or entertainment purposes.

[XR Accessibility User Requirements | Definitions of virtual reality and immersive environments](https://www.w3.org/TR/xaur/#definitions-of-virtual-reality-and-immersive-environments)

### 13.13. Augmented Reality (AR)

Augmented and mixed reality definitions vary but converge on the notion of computer-mediated interactions involving overlays on the real world. These may be informational, or interactive depending on the application.

[XR Accessibility User Requirements | Definitions of augmented reality and immersive environments](https://www.w3.org/TR/xaur/#definitions-of-augmented-and-mixed-reality)

### 13.14. Mixed Reality (MR)

### 13.15. Surface Computing

### 13.16. Spatial Computing

### 13.17. Graphical User Interface

### 13.18. User Experience (UX)

### 13.19. Input Modalities

The following are examples of some of the diverse input methods used by people with disabilities. In many real-world applications these input methods may be combined.

- **Speech** - this is where a user's voice is the main input. Using a range of speech commands, a user should be able to navigate in an XR environment, interact with the objects in that environment using their voice alone.

- **Keyboard** - this is where the keyboard alone is the user's main input. A user should be able to navigate in an XR environment, interact with the objects in that environment using the keyboard alone.

- **Switch** - this is where a single button Switch alone is the user's main input. A user should be able to navigate in an XR environment, interact with the objects in that environment using a Switch alone. This switch may be used in conjunction with an assistive technology scanning application within the XR environment that allows them to select directions for navigation, macros for communication and interaction.

- **Gesture** - this is where gesture-based controllers are the main input and can be used to navigate in an XR environment, interact with the objects in that environment, and make selections using their voice alone.

- **Eye Tracking** - this is where eye tracking applications are the main input. Using a range of commands, a user should be able to navigate in an XR environment, interact with the objects in that environment using these eye tracking applications.

[XR Accessibility User Requirements | Various input modalities](https://www.w3.org/TR/xaur/#various-input-modalities)

### 13.20. Output Modalities

The following are a list of outputs that can be available to a user to help them understand, interact with and 'sense' feedback from an XR application. Some of these are in common use on the Web and other exploratory (such as Olfactory and Gustatory.)

- **Tactile** - this is using the sense of touch, or commonly referred to as haptics.

- **Visual** - this is using the sense of sight, such as 2D and 3D graphics.

- **Auditory** - this is using the sense of sound, such as rich spatial audio, surround sound.

- **Olfactory** - this is the sense of smell.

- **Gustatory** - this is the sense of taste.

[XR Accessibility User Requirements | Various output modalities](https://www.w3.org/TR/xaur/#various-output-modalities)

### 13.21. Captions, Subtitles, and Audio Description

Closed captions subtitle are related and often interchanged terms that sometimes have overlapping definitions and implementations.

#### 13.21.1. Subtitles

- Subtitles provide a textual translation of spoken dialog. This is the default type of text track, and if used, the source language must be specified.

[MDN | WebVTT API](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)

- Different definitions of "subtitles" for different parts of the world. US & Canada are more narrowly defined than the UK where the term encompasses all types of subtitles, captions, and timed text.

[YouTube | 3Play Media Explains... SDH vs. CC: What's the Difference?](https://youtu.be/MjJLBrjWLIc?si=WPc1rknmnYjJdJxn)

#### 13.21.2. Subtitles for D/deaf and Hard of Hearing (SDH)

- Subtitles for the D/deaf and hard of hearing – more commonly known as SDH subtitles or just SDH – are timed text files that communicate all audio information.

- Traditional subtitles, or non-SDH, only reflect dialogue.

- SDH includes important non-dialogue information such as sound effects, music, and speaker identification just like captions.

- SDH may also be translated into other languages.

- SDH assumes the end user cannot hear the dialogue or understand the language spoken.

[YouTube | 3Play Media Explains... SDH vs. CC: What's the Difference?](https://youtu.be/MjJLBrjWLIc?si=WPc1rknmnYjJdJxn)

#### 13.21.3. Non-SDH Subtitles (Traditional Subtitles)

- Assumes the user can hear the audio but doesn't know the spoken language.

- Often use for language translation.

### 13.22. Captions

- Captions provide a transcription of spoken text, and may include information about other audio such as music or background noise. They are intended for hearing impaired users.

[MDN | WebVTT API](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)

#### 13.22.1. Closed Captions

- Closed captions are timed text files that communicate all audio information, including dialogue, sound effects, music, speaker IDs, and non-speech elements.

- Captions assume the end user cannot hear the audio.

- They were originally designed for D/deaf and hard-of-hearing audiences, but are commonly enjoyed by all viewers.

[YouTube | 3Play Media Explains... SDH vs. CC: What's the Difference?](https://youtu.be/MjJLBrjWLIc?si=WPc1rknmnYjJdJxn)

- Closed captioning displays the audio portion of a television program as text on the TV screen, providing a critical link to news, entertainment and information for individuals who are deaf or hard-of-hearing. The United States Congress requires video programming distributors (VPDs) - cable operators, broadcasters, satellite distributors and other multi-channel video programming distributors - to close caption their TV programs.

(The FCC does not currently regulate captioning of home videos, DVDs or video games.)

[FCC | Closed Captioning on Television](https://www.fcc.gov/consumers/guides/closed-captioning-television)

#### 13.22.2. Open Captions

- Captions that are burned into the image.

#### 13.22.3. Immersive Captions

- Captioning within XR encompasses all sounds and speech so that any deaf or hard of hearing user can perceive, understand, and fully participate in the experience to the same extent as everyone else. Therefore, the captioning must include localized speech from an identified speaker (human or otherwise) and non-localized speech, i.e., “Voice of God” audio content. Captioning must include all spatial sounds including inanimate objects sounds (e.g., weapons, appliances), animate objects sounds (e.g., footsteps, animal calls), point ambience sounds (spatialized ambient sounds that are diegetic such as a river near the user), surrounding ambience sounds (diegetic non-spatialized ambient sounds such as a crowd), and music sounds (non-diegetic background music).

[W3C | Immersive Captions Community Group | Recommendations for accessible captions in 360 degree video](https://www.w3.org/community/reports/immersive-captions/CG-FINAL-360-captions-20240412/)

#### 13.22.4. Audio Description

## 14. References

- [PUBLIC Schell Games Accessibility Matrix for Devs Outside Schell](https://docs.google.com/spreadsheets/d/1tWTime8ySqzk2DwymxHjHfJ4t6kzbmct6nhBaT1bNoI/edit#gid=849166936)

- [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/guidelines)

- [XR Access | XRA’S DEVELOPERS GUIDE, CHAPTER THREE: Accessibility & Inclusive Design in Immersive Experiences](https://xra.org/research/xra-developers-guide-accessibility-and-inclusive-design/)

- [SpoonieVR | Accessibility Chart](https://spoonievr.com/chart/)

- [Accessibility | Magic Leap](https://ml1-developer.magicleap.com/en-us/learn/guides/bp-for-accessibility)

- [Meta | VRC.Quest.Accessibility](https://developer.oculus.com/resources/vrc-quest-accessibility-1/)

- [MSF Accessibility Exploratory Group](https://metaverse-standards.org/domain-groups/)

- [Microsoft Surface 2.0 Design and Interaction Guide](https://microsoft.com)

- [U.S. Federal Communications Commission (FCC) | Closed Captioning on Television](https://www.fcc.gov/consumers/guides/closed-captioning-television#:~:text=Complete%3A%20Captions%20must%20run%20from,edge%20of%20the%20video%20screen)

- [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21/)

- [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/full-list/)
