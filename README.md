<div align="center">

# Wingman 🤖
**Cross-Platform Voice & Text AI Desktop Assistant**

[![SourceForge Downloads](https://img.shields.io/sourceforge/dt/mywingman?style=for-the-badge&logo=sourceforge&logoColor=white&color=EE6600)](https://sourceforge.net/projects/mywingman/)
[![OS - Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://sourceforge.net/projects/mywingman/)
[![OS - Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://sourceforge.net/projects/mywingman/)
[![OS - macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white)](https://sourceforge.net/projects/mywingman/)
[![Model](https://img.shields.io/badge/Model-BlenderBot--1B--Distill-orange?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/facebook/blenderbot-1B-distill)

<br />

**Wingman** is an intelligent, privacy-conscious desktop companion engineered for hands-free workflow automation and open-domain conversational AI. Powered locally by Meta's **BlenderBot-1B-Distill** model, Wingman blends system-level desktop controls, voice synthesis, and real-time information retrieval into a unified assistant that runs unobtrusively in the background.

</div>

---

## 📥 Downloads & Distribution

Pre-built binary packages and releases for Windows, Linux, and macOS are hosted on SourceForge:

👉 **[Download Wingman on SourceForge](https://sourceforge.net/projects/mywingman/)**

---

## 📑 Table of Contents

- [Core Capabilities](#-core-capabilities)
- [System Architecture & Intelligence](#-system-architecture--intelligence)
- [Supported Platforms](#-supported-platforms)
- [Quickstart & Usage](#-quickstart--usage)
- [Command Reference](#-command-reference)
- [Authors & Acknowledgments](#-authors--acknowledgments)

---

## ✨ Core Capabilities

### 💬 Conversational NLP Engine
Driven by the `facebook/blenderbot-1B-distill` transformer model, Wingman delivers empathetic, human-like dialog with contextual memory for natural conversational flow.

### 🎙️ Hands-Free Desktop Control
- **Media Automation:** Query and stream audio tracks directly on YouTube and popular streaming providers via voice commands.
- **Web Navigation:** Launch URLs, open system browsers, and navigate to target resources instantly.
- **Query Resolution:** Run automated Google searches and extract top result summaries without lifting a finger.
- **Knowledge Retrieval:** Fetch structured Wikipedia summaries and factual data directly into the assistant UI.
- **Screen Capture:** Capture high-resolution desktop screenshots instantly with simple hotkey triggers or voice inputs.

---

## 🧠 System Architecture & Intelligence

```plaintext
┌─────────────────────────────────────────────────────────┐
│                    User Input                           │
│           (Voice Command / Speech-to-Text)              │
└───────────────────────────┬─────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                 Intent Router / Classifier              │
└──────────────┬───────────────────────────┬──────────────┘
               │                           │
  [Automation / System Tasks]       [Open-Domain Chat]
               │                           │
               ▼                           ▼
┌───────────────────────────────┐ ┌───────────────────────┐
│  Desktop Automation Suite     │ │ BlenderBot-1B-Distill │
│  • Media Playback             │ │ • Contextual Memory   │
│  • Google & Wikipedia Queries │ │ • Conversational NLP  │
│  • Screen Capture Utility     │ │ • Natural TTS Voice   │
└───────────────────────────────┘ └───────────────────────┘

```
---
## 🗣️ Command Reference

| Intent | Sample Command | Action |
| :--- | :--- | :--- |
| **Music Playback** | *"Play Starboy on YouTube"* | Automates browser search and starts audio/video stream |
| **Web Navigation** | *"Open GitHub"* | Spawns system browser directly to the requested target |
| **Quick Search** | *"Google latest space missions"* | Executes Google search query and surfaces top results |
| **Encyclopedia** | *"Wikipedia Quantum Computing"* | Fetches and reads a concise structured entity summary |
| **Screen Utility** | *"Take a screenshot"* | Captures current desktop display and saves to local storage |
| **Free Chat** | *"How's your day going?"* | Routes conversation to BlenderBot NLP for dynamic dialogue |

---

## 👤 Authors & Acknowledgments

- **Vignesh S.** — [@Vignesh-72](https://github.com/Vignesh-72)
- Built on top of Meta AI's open-source [BlenderBot-1B-Distill](https://huggingface.co/facebook/blenderbot-1B-distill) model.
