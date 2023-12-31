# iPhone_sort_img_from_img_E.py
Separate img_ and img_E files for iPhone

<p>This Python program provides a graphical user interface (GUI) for moving images based on specific naming patterns within a selected folder.</p>

<h2>Installation</h2>

<ol>
    Clone the repository:
    git clone https://github.com/SurgeonTalus/iPhone_sort_img_from_img_E.py
    Navigate to the project directory:
   
    <pre><code> cd sort_img_from_img_E</code></pre>
    <li>Run the Python script:</li>
    <pre><code>python sort_img_from_img_E.py</code></pre>
</ol>

<h2>Functionality</h2>

<p>The program performs the following tasks:</p>

<ol>
    <li>Opens a GUI window allowing the user to select a folder containing images.</li>
    <li>Identifies image files with filenames starting with "IMG_".</li>
    <li>For each image file, it checks if there is a corresponding file starting with "IMG_E" and sharing the same remaining characters in the same folder.</li>
    <li>If a matching file is found, the program moves the "IMG_" version of the image to a new subfolder named "folder_IMG_" within the selected folder.</li>
    <li>The program provides feedback on the successful completion of the image moving process.</li>
</ol>

<h2>Use Cases</h2>

<p>This program can be useful in scenarios where you have a folder containing pairs of images, where one version of each pair starts with "IMG_" and the other starts with "IMG_E". The use cases include:</p>

<ul>
    <li>Organizing image collections by separating matched pairs into a dedicated subfolder.</li>
    <li>Cleaning up and structuring image directories for easier management.</li>
</ul>

<p>Feel free to customize and use this program according to your specific needs!</p>

</body>
</html>
