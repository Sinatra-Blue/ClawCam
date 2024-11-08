# ClawCam

**ClawCam** is an advanced software tool in development that detects brown crab (_Cancer pagurus_) and European lobster (_Homarus gammarus_) in video footage, providing automated insights into: 
- Species Indentification 🦞🦀
- Sex determination
- Total Length 
- Carapace Length & Width 
- Abdomen Width

## Guide Structure

| Chapter | Description 
|-----------------|-----------------|
| [Introduction](#introduction-to-clawcam)   | Gives an overview of what **ClawCam** is all about, including its goals and the benefits it brings to users considering adding AI to their workflow.    | 
| [Key Features](#key-features) | How the software will be useful. |
| [How ClawCam Works](how-does-clawcam-work?)   | Breaks down how **ClawCam** operates, with an overview of the pipeline and the processes involved. This section helps you understand the different steps taken when analyzing video footage and how the software pieces everything together.   |  
| [Project Status](project-status) | The lastest news on development and training.
| [Future Work](future-work) | Next steps for **ClawCam**.

# Introduction to ClawCam

## Overview

Information on the size and sex of crabs and lobsters is crucial for effective fisheries management and conservation efforts. **ClawCam** aims to streamline this process, aiding in:
- Assessing population age structure and growth rates
- Evaluating the overall health and sustainability of species
- Ensuring breeding populations are protected, contributing to long-term population stability and ecosystem health

## Key Features

- 👀 **Automated Detection**: Identify crabs and lobsters from video footage with minimal manual input
- 🦞🦀 **Species Identification**: Distinguish between Brown Crab & European Lobster
- 📏 **Detailed Measurements**: Obtain data on total length, carapce dimensions, and abdomen width
- 🧡 **Sex Classification**: Detect and record sex, crucial for reproductive health assessments

## How Does ClawCam Work?

### Development
![development](https://github.com/user-attachments/assets/287c5377-8402-4dc8-8f8f-07f6287daf68)

The **ClawCam** development pipeline follows a structured process to handle and analyse video footage from fisheries or processing centers. Here's how the pipeline works:

1.  _Video Input_: The process starts by receiving video footage directly from fishermen or processing centers. This footage serves as the raw data for analysis.
2.  _Frame Extraction_: The video is processed to extract individual frames, preparing them for further analysis.
- _**Parallel Processes**_:
3.  _Frame Evaluation_: Each extracted frame is analysed and classified as either a 'good' frame or a 'bad' frame based on quality and content. This information is logged into an Excel sheet for easy reference.
4.  _Ground Truth Linking_: Simultaneously, individual lobsters in the frames are linked to ground truth data, such as measurement details, sex, and other relevant biological information. This ensures that each lobster detected in the footage is paired with accurate data for validation and training.
5.  _Data Integration_: Finally, the two Excel sheets — one containing the frame evaluations and the other containing the linked ground truth data — are combined. This integrated dataset forms a comprehensive resource that aids in training the model and validating its output.

### Deployment
![deployment (1)](https://github.com/user-attachments/assets/f93e0b83-7851-4912-a377-73cda0da03f0)

1. _Video Input_: Just like in the development stage, video footage is taken directly from fishermen or processing centers, acting as the source data for the pipeline.
2. _Frame Extraction_: The incoming video is broken down into individual frames to make the data manageable for analysis.
- _**Parallel Processes**_:
3. _Frame Evaluation_: Each frame is assessed to determine whether it is a 'good' or 'bad' frame. This evaluation is recorded in an Excel sheet to ensure transparency and easy tracking.
4. _Lobster Detection_: Unlike the development stage, frames are now linked to detected lobsters without the need for ground truth data. This process focuses on identifying and assigning each lobster within the frame for analysis.
5. _Excel Sheet Compilation_: The results from the frame evaluations and the lobster detection process are combined into a comprehensive Excel sheet. This sheet captures the frame quality and assigns lobsters accordingly.
6. _Data Filtering_: The compiled sheet is filtered to isolate and retain only 'good' frames. This ensures that only high-quality, usable frames move forward in the pipeline.
7. _Model Input_: The filtered set of good frames is then fed into the **ClawCam** model for further processing, enabling automated detection, measurement, and analysis of crabs and lobsters.

### Postprocessing

## Project Status

**ClawCam** is in the early stages of development. Currently, we are focusing on:
- Initial data collection and automated annotations
- Setting up a robust testing framework
- Integrating core functionalities for species detection and measurements.

_Updates on progress and milestones will be regularly added here_

## Future Work

Upcoming development plans include:
- Enhancing the detection accuracy with additional training data
- Implementing user feedback for improved usability
