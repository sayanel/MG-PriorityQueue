## Explain Big-O notation in simple terms.

In simple terms, Big-O notation provides a common language to describe how the performance of an algorithm will scale. It uses expressions like O(n^2) or O(log n) to represent the relationship between the size of the input (n) and the time it takes to solve the problem. For example, O(n^2) means that as the data size doubles, the time it takes quadruples, while O(log n) indicates that the time grows much slower than the size of the data.
By using Big-O notation, we can compare different approaches and choose the most efficient one for handling larger data sets. It helps us make informed decisions about algorithm design and optimization. So, when someone talks about Big-O notation, they're essentially discussing how quickly an algorithm's performance deteriorates or improves as the amount of data increases, allowing us to select the most suitable approach for our problems.


## What are the most important things to look for when reviewing another team member's code?
To me, the most important things to look for when reviewing another team member code are:
- Functionnality: the code achieves its intended purpose.
- Readability: the code is easy to read and understand, with meaningul variable and function names, respect pep8 formatting and has good comments..
- Reusability: the code is well organized, modular and respect the separation of concerns.
- Error handling: errors are not going to pass silently and the meaningul one are getting back to the user or logged for debugging purposes. Look for edge cases.
- Efficiency: check that there is no algorithm bottleneck and if some code could be easily simplified or improved.
- The PR is passing the tests and cheks.


## Describe a recent interaction with someone who was non-technical. What did you need to communicate and how did you do it?
An artist was using our Multishot tool, this tool allows him to create multiple cameras in the same scene. This tool is strongly using USD technology and this artist was experiencing a "Stronger Opinion" error whenever he was trying to translate/rotate/scale an object.
To explain to him what was happening I had to explain how Layers and Overs work in USD. 
It went something like this:

In the Multishot, there are multiple cameras that capture different shots and each camera has its own specific frame range. The tool allows you to create overlays (Overs or Tweaks) on objects within these different camera views. This means you can have different overlays for the same object in different cameras because they don't share the same frame range.
However, there is also a main layer that is not tied to any specific camera and has a "lower" priority. When you try to create an overlay in the main layer, it wants to apply the overlay across the entire frame range of the scene. But this causes a problem because the object already has an overlay created specifically for a particular camera's frame range.
The "Stronger Opinion" error occurs because the system recognizes that there is a conflict. It understands that creating an overlay in the main layer would result in overlapping and conflicting overlays across different camera views. To maintain consistency and avoid conflicts, the system prevents you from creating overlays in the main layer that would affect the entire frame range. 

Basically, when trying to communicate technical concepts to artists I try to avoid technical jargon and complex terms. If I can I will use analogies, metaphors or diagrams to provide visuals. I would breakdown the concept into smaller parts, encourage questions from their end and try to be as clear as possible.


