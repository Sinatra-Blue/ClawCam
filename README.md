# ClawCam

**ClawCam** is an advanced software tool in development that detects brown crab (_Cancer pagurus_) and European lobster (_Homarus gammarus_) in video footage, providing automated insights into: 
- Species Identification 🦞🦀
- Sex determination
- Total Length 
- Carapace Length & Width 
- Abdomen Width

## Guide Structure

| Chapter | Description 
|-----------------|-----------------|
| [Introduction](#introduction-to-clawcam)   | Gives an overview of what **ClawCam** is all about, including its goals and the benefits it brings to users considering adding AI to their workflow.    | 
| [Key Features](#key-features) | How the software will be useful. |
| [How ClawCam Works](how-does-clawcam-work?)   | Breaks down how **ClawCam** operates, with an overview of the pipeline and the processes involved. This section helps you understand the different steps taken when analysing video footage and how the software pieces everything together.   |  
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
![development (2)](https://github.com/user-attachments/assets/ed694331-2ee5-4d46-94c2-96d2c8462d40)


The **ClawCam** development pipeline follows a structured process to handle and analyse video footage from fisheries or processing centers. Here's how the pipeline works:

1.  _Video Input_: The process starts by receiving video footage directly from fishermen or processing centers. This footage serves as the raw data for analysis.
2.  _Frame Extraction_: The video is processed to extract individual frames, preparing them for further analysis.
3.  _Frame Selection_: Each extracted frame is analysed and classified as either a 'good' frame or a 'bad' frame based on quality and content. This information is logged into an Excel sheet for easy reference.
4.  _Lobster Detection_: Individual lobsters are detected within each frame, and their locations are identified for further analysis.
5.  _Ground Truth Linking_: Simultaneously, individual lobsters in the frames are linked to ground truth data, such as measurement details, sex, and other relevant biological information.
6.  _Data Integration_: The two Excel sheets — one containing the frame evaluations and the other containing the linked ground truth data — are combined. This integrated dataset forms a comprehensive resource that aids in training the model and validating its output.

**Feeding The Model and Iterative Training**

7. _Feeding Data to the Model_: The filtered set of good frames, containing all necessary lobster information, is fed into the **ClawCam** model.
8. _Model Prediction_: The model uses the provided good frames to make predictions on the species, measurements, sex, and other relevant details of the lobsters detected in each frame.
9. _Error Function_:
- Model Evaluation: The predicted outputs from the model are compared to the actual ground truth information using an error function.
- Error Calculation: The error function calculates the difference between the predicted data and the actual, ground truth data, determining how far off the model's predictions are.
10. _Iterative Training Loop_: The model uses the calculated error to adjust its parameters, aiming to minimise this difference. The corrected parameters are then used in the next round of training, and the cycle continues, gradually improving the model's accuracy.

![Resize image project](https://github.com/user-attachments/assets/542c5265-00e7-4c22-b872-87473c2cc2c8) ![Resize image project (2)](https://github.com/user-attachments/assets/b9890a80-ed46-4f59-93a9-9fc04210f439)

                      Good Frame                              |                      Bad Frame

  
### Deployment
![deployment 2 (3)](https://github.com/user-attachments/assets/3b7898e1-ebd6-426c-9ed6-d5e19dac0147)
1. _Video Input_: Just like in the development stage, video footage is taken directly from fishermen or processing centers, acting as the source data for the pipeline.
2. _Frame Extraction_: The incoming video is broken down into individual frames to make the data manageable for analysis.
3. _Frame Evaluation_: Each frame is assessed to determine whether it is a 'good' or 'bad' frame. This evaluation is recorded in an Excel sheet to ensure transparency and easy tracking.
4. _Lobster Detection_: At the same time, frames are processed to detect and identify individual lobsters. Unlike the development stage, this step does not require ground truth data but focuses purely on recognising and assigning lobsters for further analysis.
5. _Excel Sheet Compilation_: The results from the frame evaluations and the lobster detection process are combined into a comprehensive Excel sheet. This sheet captures the frame quality and assigns lobsters accordingly.
6. _Filter for Good Frames_: The compiled Excel sheet is filtered to include only the 'good' frames that contain identified lobsters. This step ensures that only high-quality frames are sent to the model for further analysis, maximising the reliability of the predictions.

**Model Optimisation**

7. _Feeding the Model_: The filtered set of good frames is fed into the **ClawCam** model for analysis. The model processes the frames to predict important details about the lobsters, such as species, measurements, and sex.
8. _Model Prediction_ and _Post-Processing_:
- Initial Prediction: The model generates predictions for each detected lobster based on the processed frames.
- Post-Processing: The predicted information is then fed into a post-processing stage. Here, statistical modeling techniques are used to refine the results, ensuring that a single, consistent value is obtained for each piece of information per lobster. This helps eliminate inconsistencies that may arise from multiple frames, providing a more accurate overall prediction for each lobster.
9. _Final Predicted Data_: After post-processing, the final predicted information is generated, ready for use in fisheries management and conservation efforts. The post-processing step may be repeated if necessary to further optimise and refine the predicted outputs.

### Postprocessing

## Project Status

**ClawCam** is in the early stages of development. Currently, we are focusing on:
- Initial data collection and automated annotations
- Setting up a robust testing framework
- Integrating core functionalities for species detection and measurements.

_Updates on progress and milestones will be regularly added here_

## Supplementary Materials
[Camera Instructions.docx](https://github.com/user-attachments/files/17950489/Camera.Instructions.docx)


## Future Work

Upcoming development plans include:
- Enhancing the detection accuracy with additional training data
- Implementing user feedback for improved usability
