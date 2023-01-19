This repo contains the files and the final report as part of the course "Autonomous Vehicle Navigation" at UCSD 

Autonomous Vehicle Navigation using Nvidia Jetson Nano onboard processor; MySQL for database management; multi-threading for accessing a database on Linux Platform via MAC or Windows OS. The goal is to simulate the scenario where you as a customer can request for an autonomous public transport vehicle to stop at a particular terminal. The request will be logged into central server that can be accessed by the vehicle. Upon stopping at the terminal, the vehicle automatically removes any request for that terminal from central server (picks up customer), and continues the ride around a track. 

# Summary of Objectives :
1. Mold a plastic case to hold the Nvidia Jetson Nano processor using 3D printing
2. Assemble the additional components such as Nano board with the case, battery to power the Nano board, Camera to collect images on a remote controlled toy car.
3. Drive the car around the track using the remote control to collect images. 
4. Train a model offline using supervised learning (input = images from the camera, output = remote control commands)
5. Test the autonomous navigation capability of the car on the same track using the trained model.
6. Introduce a real case scenario : Autonomous public transport system
7. Implement additional components to test the real case scenario

      a. mySQL implementation for adding request or removing request from a database table stored in a server.
      
      b. Additional image processing for color detection [ we failed to implement real time string recognition using Tesseract due to low processing power ] along with images used for autonomous nagivation.
      
8. Document the final implementation details, challenges, and prepare git repository.


# Source Code information :
## Code for Training and implementing model for Autonomous Driving : 
https://github.com/wingz0c/ucsdrobocar04

## Code for optical character recognition : 
This repo contains source code for text recognition from images using Tesseract

## Code for mySQL implementation : 
The document in repo https://github.com/niil87/Autonomous_Navigation_UCSD/blob/master/ECE-MAE-148%20Summer%202019%20Team4.pdf contains necessary information

