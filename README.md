<div align="center">
  <h1>🐍 My Python Portfolio</h1>
  <p><em>A growing collection of scripts and automation tools built while mastering Python.</em></p>

  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Focus-Backend%20%26%20Automation-orange" alt="Focus">
  <img src="https://img.shields.io/badge/Status-Active-green" alt="Status">

  <p>
    <a href="#projects">Projects</a> • 
    <a href="#debugging">Bug Tracker</a> • 
    <a href="#roadmap">Roadmap</a> • 
    <a href="#setup">Setup</a>
  </p>
</div>

<hr>

<h2 id="projects">🗂️ Project Showcases</h2>

<h3>🛠️ Core Utilities & Math</h3>
<table width="100%">
  <tr>
    <th align="left">Project</th>
    <th align="left">Description</th>
    <th align="left">Key Concept</th>
  </tr>
  <tr>
    <td><a href="calculator.py">🧮 Calculator</a></td>
    <td>CLI calculator for basic operations (+, -, *, /) with a zero-division guard.</td>
    <td><code>If/Elif Logic</code></td>
  </tr>
  <tr>
    <td><a href="temperature%20convertor.py">🌡️ Temp Converter</a></td>
    <td>Converts Celsius to Fahrenheit using standard formulas.</td>
    <td><code>Data Conversion</code></td>
  </tr>
  <tr>
    <td><a href="simple%20interest.py">💰 Simple Interest</a></td>
    <td>Calculates interest based on Principal, Time, and Rate.</td>
    <td><code>Arithmetic Ops</code></td>
  </tr>
  <tr>
    <td><a href="circle.py">⭕ Circle Area</a></td>
    <td>Calculates the area of a circle using $\pi = 3.14$.</td>
    <td><code>Math Logic</code></td>
  </tr>
  <tr>
    <td><a href="for%20rectangle.py">📐 Geometry</a></td>
    <td>Computes both area and perimeter of a rectangle based on user input.</td>
    <td><code>F-Strings</code></td>
  </tr>
  <tr>
    <td><a href="leap%20or%20not.py">📅 Leap Year</a></td>
    <td>A script to determine if a year is a leap year based on divisibility by 4.</td>
    <td><code>Modulo Operator</code></td>
  </tr>
  <tr>
    <td><a href="which%20is%20greater.py">🆚 Comparison</a></td>
    <td>Evaluates two numbers to find the greater value or check for equality.</td>
    <td><code>Comparison Ops</code></td>
  </tr>
</table>

<h3>🎓 Academic & Data Management</h3>
<ul>
  <li><strong><a href="forclass.py">📊 Marks Calc</a>:</strong> Aggregates marks from 5 subjects to calculate total score and percentage.</li>
  <li><strong><a href="grade.py">🏅 Grade Pro</a>:</strong> Assigns letter grades (A+ to B) based on average performance.</li>
  <li><strong><a href="tree.html">🌳 Shah Dynasty</a>:</strong> An interactive SVG/HTML family tree tracing the Royal House of Shah to the Dhankuta branch.</li>
</ul>

<h3>🌐 Advanced & Security Simulations</h3>
<ul>
  <li><strong><a href="api%20connect.py">🎮 Poke-Fetch</a>:</strong> Connects to PokéAPI to retrieve Pokémon stats like ID, weight, and height.</li>
  <li><strong><a href="unit.py">⚡ Utility Bill</a>:</strong> Tiered electricity billing simulation based on unit consumption (Rs. 30 / Rs. 5 / Rs. 7).</li>
  <li><strong><a href="account.py">🔐 Gatekeeper</a>:</strong> A simple admin login simulation with password verification.</li>
  <li><strong><a href="idk.py">🐢 Turtle Art</a>:</strong> A visual script using the <code>turtle</code> module to draw red-outlined, yellow-filled shapes.</li>
</ul>

<hr>

<h2 id="debugging">⚠️ Known Issues & Debugging Practice</h2>
<p>These scripts are part of a learning journey and contain "intentional bugs" to practice debugging:</p>
<ul>
  <li><strong>API Connection:</strong> In <code>api connect.py</code>, the <code>status_code</code> check is placed after a <code>return</code> statement, preventing it from running.</li>
  <li><strong>Grade Calculation:</strong> In <code>grade.py</code>, the average is currently calculated by multiplying marks rather than adding them.</li>
  <li><strong>Simple Interest:</strong> The formula currently lacks the <code>/ 100</code> division needed for mathematical accuracy.</li>
</ul>

<hr>

<h2 id="roadmap">🚀 Roadmap</h2>
<ul>
  <li>[ ] <strong>🛡️ Error Handling:</strong> Implement <code>try/except</code> blocks to handle non-numeric inputs gracefully.</li>
  <li>[ ] <strong>🔒 Secure Auth:</strong> Upgrade <code>account.py</code> to use hashed passwords instead of plain text.</li>
  <li>[ ] <strong>🖥️ Desktop UI:</strong> Rebuild the Calculator with a graphical interface using <strong>Tkinter</strong>.</li>
  <li>[ ] <strong>📁 Automation:</strong> Create a script that automatically sorts files in a directory by extension.</li>
</ul>

<h2 id="setup">🏁 How to Run</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/yourusername/python-portfolio.git</code></pre>
  </li>
  <li>Install dependencies (for API projects):
    <pre><code>pip install requests</code></pre>
  </li>
  <li>Execute a script:
    <pre><code>python calculator.py</code></pre>
  </li>
</ol>

<hr>

<div align="center">
  
</div>
