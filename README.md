# Ally---The-Helper-Bot
Ally- The Helper Bot is a voice based assistant that makes use of Neural Networks and Speech Recognition to create a basic therapist. It interacts with people dealing with depression. It aims to bridge the gap between computerized and live therapy. It uses a scale to predict the client's emotion and converses by calculating their depression intensity and providing support by giving intensity-driven recommendations. Ally may suggest a movie, music or a book to elevate the symptoms of depression, make use of Cognitive Behavioural Therapy (CBT) to converse further with the patients and even alert their emergency contacts in case of severe intensities of symptoms.
## Ally in brief - a flow-chart:

#### Modules:
1. Chatbot: 
   - 3 Neural networks. one for classifications, two RNNs for conversation.
   - A system for administering CBT that can be a pre-feeded dialog system.
2. Controller interface for devices to be operated, like television, music player, computer etc.
3. Voice to text interface.
4. Text to speeech interface.
5. Log generation for patient's data.
6. Fail-safe module(extreme cases like suicidal/self-harm thoughts and other such conversation). 
7. Voice analysis.
8. Facial analysis(if applicable).

#### Architecture for Chatbot: 

!(/chatbot_flow.PNG)

> **Neural network-1:** _A network that analyses the text input and classifies it under 3 categories, finally decides upon what system to use:_
> - Neutral conversations: _Where the system functions like a normal chatbot(**Neural network-2**)._
> - Weak-Emotion conversation: _Where the system generates emotional responses(**Neural network-3**)._
> - Strong-Emotion conversation: _where administering subtle CBT is required._
