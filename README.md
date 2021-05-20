# Artificial-Intelligence-and-COVID-19-Deep-Learning-Approaches-for-Diagnosis-and-Treatment
final year IEEE project

Introduction

    Several countries are under lockdown today because of the exponentially increasing number of COVID-19 cases.
    The one factor that can contain the virus, apart from an increase in hygiene and social distancing, is early
    diagnosis to effectively isolate carriers of the disease.

    Limited availability of viral testing kits and the time-consuming nature of these tests is making radiology
    come to the forefront of diagnosis. The report given by them is turning out to be a key element in deciding
    the treatment. 
    
    COVID-19’s rate of transmission depends on our capacity to reliably identify infected patients, with a low
    percentage of false negatives. Timely detection of the disease enables the implementation of all supportive
    care required by the affected patients as well as isolation to prevent spread.

    In COVID-19 scenario, covid infected people is easily captured through their property like fever, blowing
    nose ,head pain and body pain etc. but in this COVID 2.0 ,we found some of the people who have no any
    activity like this ,they also effected with covid . 
    
    we will do test to find the covid positive people but that test took 3 days or more time to find this .
    so for solving that solution we use xray and ct-scan report to find the effected people within one hour.
    Here we used more than 100 images dataset for postive and 100 plus images for covid negative and use 
    that image to find covid positive patient. It will give 97% accuracy.
    
 PROPOSED  SYSTEM

    AI approaches can be useful in eliminating disadvantages such as insufficient number of available RT-PCR
    test kits, test costs, and waiting time of test results.
    
     It is  simple, accurate, and fast AI models may be helpful to overcome this problem and provide timely
     assistance to patients. 
     
     The proposed model has an end-to-end architecture without using any feature extraction methods, and it
     requires raw chest X-ray images to return the diagnosis. 
     
    The models can be readily used in healthcare centers. There is no need to wait long hours for the
    radiologists to screen  the images. Thus, healthcare workers and patient  relatives can focus on
    isolation of suspicious cases so that treatment can begin.
    
    The spread of the disease can be significantly reduced. The patients can seek a second opinion if they
    are diagnosed as positive by our  system. Hence,  waiting time  can  be  significantly  reduced,
    and  it  will alleviate  clinician workload.
    
ADVANTAGES

    Take less time compare to exisiting system
    Less costly compare to exisiting system
    More Accurate upto 97% 
    User Friendly
    
MODULE DESCRIPTION

    1. USER
    2. DETECTION

    USER
      
        -> Guidance to Use
        -> Upload X-Ray images
        -> View X-ray report
        -> Upload CT-Scan
        -> View CT report
        -> View Analysis
    
    DETECTION

        -> Collection chest X-ray or CT images of patient
        -> Normalize the data(Images)
        -> Resizing of images
        -> Classifying the images
        -> Evaluation
    
IMPLEMENTATION

    HARDWARE  REQUIREMENTS 
        System	            : Pentium V 
        Hard Disk        	  : 40 GB.
        Monitor		          : 15 VGA Colour.
        Ram		              : 512 Mb.

    SOFTWARE  REQUIREMENTS
        Operating system 		: 	Windows 10
        Coding Language		  :	  Python
        Platform			      :	  Pycharm
        
     LIBRARY REQUIREMENTS
         flask
         tensorflow
         pillow

    MODEL REQUIREMENT
        VGG16 model
        Convolutional neural network (CNN)
        
CONCLUSION

    This project demonstrated that a deep transfer learning is feasible to detect COVID-19 disease
    automatically from chest X-ray or CT-scan by training the learning model with chest X-ray and
    CT images mixed with COVID-19 patients, which may help doctors more effectively make their
    clinical decisions.
    
    This project also gives an insight to how transfer learning was used to automatically detect
    the COVID-19 disease. 
    
    Due to current pndemic situation, this system can be widely used for detecting covid patient
    as early as possible.It can be used by any users, radiologists where has its need .
    
FUTURE SCOPE

    Right now we are using only image data (i.e., X-rays and CT) —so in future it should leverage
    multiple data sources not limited to just images, including patient vitals, population density
    etc. Image data by itself is typically not sufficient for these types of applications.

    we will need more data at various stages, with the COVID-19 X-rays taken when the patients
    present several symptoms.

    I will try to add some more images for MRI etc to detect COVID desease.

    I will try to improve the Accuracy  using different model like HSGO model
    (Hybrid-Social-Group-Optimization-algorithm),Inceptionv3, DenseNet121 etc.

    I will try to show the accuracy and effected part of chest also.
    
REFERENCES

    https://ieeeaccess.ieee.org/featured-articles/aiandcovid19_deeplearning/
    




     





