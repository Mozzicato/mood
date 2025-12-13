# Therapist-Style Emotion-Based Chatbot (Design Document)

## 1. Project Overview

### Project Name (Working)

TheraMood AI (name can be changed)

### Tagline

A therapist-style AI chatbot that helps users explore their emotions through guided, empathetic conversation.

### Hackathon

PeerBridge Mental Health Hacks 2025

### Tracks

* Tech for Empathy
* Digital Safe Spaces

### Target Audience

* Youth aged 15–25
* Users seeking emotional support, reflection, and guidance

---

## 2. Problem Statement

Many young people experience intense emotions (sadness, anger, overwhelm, depression) but lack:

* A safe, judgment-free space to talk
* Access to immediate emotional support
* Skills to explore and understand their feelings

Cultural stigma, fear of judgment, and limited mental health resources prevent open expression.

---

## 3. Solution Summary

This project is a **therapist-style conversational chatbot** that:

* Starts with **emotion-based selection**
* Adapts its conversation style based on the chosen emotion
* Uses **therapy-inspired techniques** (CBT, reflective listening)
* Guides users through structured emotional exploration

The chatbot does **not** diagnose or replace professional therapy.

---

## 4. User Experience Flow

### 4.1 Homepage / Emotion Selection

The homepage displays a grid of **colored emotion cards**:

* 😊 Happy (Yellow)
* 😢 Sad (Blue)
* 😡 Angry (Red)
* 😰 Overwhelmed (Purple)
* 😞 Depressed (Gray)
* ✍️ Describe (Neutral)

Each card is clickable and represents the user’s current emotional state.

---

### 4.2 Emotion Selection Logic

When a user selects an emotion:

* The system stores the selected emotion
* The chatbot switches to a **therapist-style mode** specific to that emotion

Example system state:

```
Selected Emotion: Sad
Therapy Mode: Emotional reflection + gentle CBT questioning
```

---

### 4.3 Chat Interface

The chat interface includes:

* AI therapist messages
* User text input
* Optional action buttons

Initial AI message example:

> "I’m here with you. Can you tell me more about what’s been making you feel sad?"

---

### 4.4 Conversation Flow

Each conversation follows a structured therapeutic loop:

1. **Acknowledge Emotion**
2. **Reflect & Validate**
3. **Explore (Open-ended questions)**
4. **Reframe or Insight**
5. **Offer Optional Tools**

The user controls how deep the conversation goes.

---

## 5. Therapist-Style Conversation Design

### 5.1 Core Techniques Used

The chatbot explicitly uses:

* Active listening
* Emotional reflection
* Cognitive Behavioral Therapy (CBT)-inspired questioning
* Gentle cognitive reframing

---

### 5.2 Emotion-Specific Behavior

#### Sad / Depressed

* Focus on validation
* Explore loss, motivation, self-worth
* Avoid labels or diagnosis

Example:

> "When you say everything feels heavy, what does that look like in your daily life?"

#### Angry

* Normalize anger
* Explore triggers
* Redirect toward healthy expression

#### Overwhelmed

* Break problems into smaller parts
* Grounding and prioritization

#### Happy

* Reinforce positive coping
* Encourage reflection and gratitude

#### Describe (Custom)

* Emotion is inferred from text
* Mixed therapeutic approach applied

---

## 6. Safety & Ethics Design

### 6.1 Disclaimer

Displayed clearly in the interface:

> "This chatbot provides emotional support using therapy-style conversation techniques. It is not a licensed therapist and does not replace professional mental health care."

---

### 6.2 Crisis Detection

The system monitors for high-risk phrases (e.g., self-harm, suicidal ideation).

If detected:

* AI responds with empathy
* Encourages reaching out to trusted people or local support services
* Avoids panic or authoritative tone

Example:

> "I’m really glad you shared this with me. You deserve support beyond this space. Please consider reaching out to someone you trust or a local support service."

---

## 7. Technical Architecture

### 7.1 Frontend

* Framework: React / Next.js
* Styling: Tailwind CSS
* Components:

  * EmotionCard
  * ChatWindow
  * MessageBubble
  * ActionButtons

---

### 7.2 Backend

* API: FastAPI (Python) or Node.js
* Handles:

  * Emotion state
  * Prompt construction
  * AI responses

---

### 7.3 AI Layer

Core system prompt:

```
You are a therapist-style mental health chatbot.
Use empathy, reflection, and CBT-inspired questioning.
Do not diagnose or prescribe treatment.
Ask gentle open-ended questions.
Encourage emotional insight and healthy coping.
```

Emotion-specific prompts are appended dynamically.

---

## 8. Data & Privacy

* No user accounts required
* No long-term data storage (optional local storage only)
* Conversations remain private

---

## 9. Limitations

* Not a substitute for professional therapy
* No clinical diagnosis
* Not designed for emergency intervention

---

## 10. Future Enhancements

* Multi-language support
* Cultural tone customization
* Voice-based interaction
* Mood tracking over time

---

## 11. Hackathon Alignment

This project aligns with PeerBridge goals by:

* Breaking stigma around emotional expression
* Creating safe digital spaces
* Using AI responsibly for empathy and mental health

---

## 12. Conclusion

This therapist-style chatbot combines accessible UI, ethical AI design, and evidence-based therapeutic conversation to support youth mental well-being in a safe, inclusive, and culturally adaptable way.
