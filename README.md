This repo contains the files and the final report as part of the course "Autonomous Vehicle Navigation" at UCSD 

Autonomous Vehicle Navigation using Nvidia Jetson Nano onboard processor; MySQL for database management; multi-threading for accessing a database on Linux Platform via MAC or Windows OS. The goal is to simulate the scenario where you as a customer can request for an autonomous public transport vehicle to stop at a particular terminal. The request will be logged into central server that can be accessed by the vehicle. Upon stopping at the terminal, the vehicle automatically removes any request for that terminal from central server (picks up customer), and continues the ride around a track. 

Summary of Objectives :
1. Mold a case to hold the Nvidia Jetson Nano processor using 3D printing
2. Assemble the components additional components on toy car like a battery to power the Nano board, RF transciever for remote control of the car, Camera to collect images. 
3. Drive the car around the track using remote control to collect images. 
4. Train a model offline using supervised learning. (input = images from the camera, output = remote control commands)
5. Test the car on the track using a trained model. 
6. Introduce a real use case scenario : Autonomous public transport system
7. Implement additional components 

      a. mySQL implementation for adding request or removing request from a database table stored in a server.
      
      b. Additional image processing for color detection [ we failed to implement real time string recognition using Tesseract due to low processing power ] along with images used for autonomous nagivation.


This repo contains source code for text recognition from images. 

There is another repo that contains the source code for autonomous driving. https://github.com/wingz0c/ucsdrobocar04
