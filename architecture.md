# Architecture Overview

## Vision Module
- Uses YOLO or SAM models to extract human pose keypoints from video frames.
- Provides real-time feedback on user exercise form.

## AI Logic Module
- Processes pose keypoints and compares them with ideal exercise forms.
- Uses Claude API to generate personalized advice and motivation messages.

## Quantum Optimization Module
- (Experimental) Uses quantum algorithms to optimize workout schedules and intensity.
- Implemented with IBM Qiskit or similar platforms.

## Automation Module
- Uses n8n to automate progress tracking, reminders, and notifications.
- Integrates with messaging apps and calendars for user convenience.

## Backend
- FastAPI server to manage communication between modules.
- Stores user profiles, session history, and feedback logs.

## Frontend
- Web application built with React.
- Displays live video feed, form correction feedback, and workout stats.