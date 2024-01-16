# Gibberish Detector : A easy way of detecting Frauds
## Overview
The Gibberish Detector is a Python script designed to classify names or email usernames as either gibberish or non-gibberish. The primary application of this project is in fraud detection, where it proves effective in identifying potential fraudulent accounts. Fraudsters often use randomly generated names and emails for their scams, and this script aims to mitigate such activities by preventing the creation of accounts with gibberish details.

## Background
Fraud detection is a critical aspect of online systems, and one common pattern observed is the use of gibberish names and email usernames by scammers. The Gibberish Detector addresses this issue by implementing algorithms to identify and classify such entries, reducing the likelihood of fraudulent activities.

## Requirements
There is no specific package requirement for running this project.
The python packages used belongs to default installation package.

## Usage
To use the Gibberish Detector, simply import the script and call the main function, it will ask for a input string. Enter it and it should give a output stating if it's a gibberish or non gibberish.

## Working Mechanism
The Gibberish Detector employs four methods to classify input strings:
1. **String Search with Common Indian Names**: Utilizes a list of common Indian names to identify and score potential non-gibberish names.
2. **Average Distance Between Letters on a Keyboard**: Scores consecutive letters based on their proximity on a keyboard.
3. **Vowel Count**: Sets a threshold for the number of vowels, classifying words with more than two vowels as non-gibberish.
4. **Number of Unique Characters**: Considers the percentage of unique characters in a word, classifying it as gibberish if below the 73% threshold.

The model aggregates the individual results from each method and classifies the input based on the majority outcome. In the case of a tie, the model defaults to classifying the input as gibberish.

## Accuracy
In our use case, the Gibberish Detector demonstrates a commendable accuracy of 73%, significantly enhancing fraud prevention in our systems.

## Customization
Users can enhance the functionality of the Gibberish Detector by adding more names to the names CSV file, tailoring the model to detect names from other regions. Also, might as well add many more formula to make this model more robust.

## Conclusion
The Gibberish Detector offers a practical solution to the challenge of identifying fraudulent accounts by effectively classifying gibberish and non-gibberish names and email usernames. Its modular design allows for easy customization, and its success in reducing fraud in our systems demonstrates its effectiveness as a valuable tool for online security.
