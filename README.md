# Selenium-Testing

**PROJECT UNDER CONSTRUCTION**

This is a **Selenium-Pytest** demo. In this project I apply tests in demo site https://demoqa.com by **ToolsQA.com**, in pages:
        /automation-practice-form and /login.<br/>
Tests setup is for **Chrome**, **Firefox** and **IE** browsers and the choice is done by terminal. **pytest -v -s --driverName=chrome**.<br/>
The inputs are static, but are about to be inserted dymamically.<br/>
The main taget is:
  * by the **assertion**, to compare the expected with the actual outcomes
  * create a **report** of test enviroment,test cases test pass/fail. Also give an automated screenshot file with the browser test result
  * deliver a **error-warning** level report.


**TEST ARCHITECTURE**

  * The **driver** pytest requests included in **conftest.py** file<br/>
  * All tests are included in **tests** package.<br/>
  * A **BaseClass** class place in order driver call and test plans, in BaseClass package.<br/>
  * Αfter the plan is ready, we call BaseClass in **test_main**. **!!!** In test_main we can call and another test plans if we want with other requests.<br/>
  * test_main is ready to be executed as pytest.

<!-- Diagram editor -->
<!DOCTYPE html>
<html>
<head>
<title>Untitled Diagram.jpg</title>
<meta charset="utf-8"/>
</head>
<body><div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;www.diagrameditor.com\&quot; modified=\&quot;2021-09-15T20:03:25.732Z\&quot; agent=\&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0\&quot; etag=\&quot;mhb7XbFHIoMXpvid_Yto\&quot; version=\&quot;12.1.3\&quot; pages=\&quot;1\&quot;&gt;&lt;diagram id=\&quot;NBHB_bB2qGBYu4o_yeA6\&quot; name=\&quot;Page-1\&quot;&gt;5Zpdc5s4FIZ/jS/rERKfl7X7sZ3OznY2u7PtVUYG2WiDkSPk2O6vrxQkA4LEOLWxm14ZHcEBvefhIB15hKbL7UeOV+mfLCHZCIJkO0LvRhA6ALryR1l2pcUF2rDgNNEnVYYb+p00jWuakKJhEoxlgq6axpjlOYlFw4Y5Z5vmaXOWNW+6wgvSMtzEOGtb/6OJSEtrCIPK/gehi9Tc2fGjsmeJzcmgNBQpTtimZkLvR2jKGRPl0XI7JZnSzshSXvfhid79g3GSiz4XRPnD57/hJ/LvbRj/Pwnje6f48AZ5pZsHnK31iPXTip2RgLN1nhDlxRmhySalgtyscKx6NzLm0paKZaa796NUjTnNsinLGH90hBKPhImrThKc3ZFaTwhnyPdlj34awgXZPjlOZ6+epI6wJRF8J0/RFyAjuAYOehq4TRU/X5vSeuh0SLEmZrH3XIkqD7Sux2jsd2jsZ/K2k4Q+yMOFOlximt8KUgjTJ+9V625FRQoknpH+JEK6TSHdqCWkMdWFNPqfXEgYDQgrcSSuQReskR8gfCJYIYANjRH0Whp7aEhYQR9YZbadXxWrEPiWjuCyrDrukIkVk3Aed7HqxyGZzU+jsdOUGLphS2LH6FnXOHDOpPErTAfo4KfLMaQPkg7any712t+qKVhxj2eM3RWXeNuDgx+mqEOl873s8NWTaPS8GIkOehbFOePLKyAxctokBkOS2J7P/yNVKh4HFd+pxU4PkRpg5SwnFoXahDO6yGUzlmIRaZ8oKalcO73VHUuaJOo2nbhXLwQ4x+TV4he15wPhoCkieIXzgfDKJgRmDIOIPJ8TP+4UOQmiGQAnEjnwrmxKYDRtrhDwUkmXz4rV47iPbYMJLsg0w8UlphNOEF3XfAK2v3VrQTMqKPn9MrkTorH1DnQl80ELET2qZiRP3qr6o1JVcU3jZmjk6Pnuq2y8AWMAoLF8UyqOfRQaw7ut1rVs7eqtL4RTOSIVsdK4peKr8S+PS2eeblWeVMM4Kh+cJK0yqBUfOTi25jF5RhYdAoH5goiDGaQd8HrNo+OzYWycZFjQh+bzdsVY3+ELo3IkFU/21MC3MCnHqa+CtYKq7SiwHLmWo1KIlqNH5PbD/gkKe0wpelMImgAG3iH+LouaWXFdO2teM3MhUxY6njVrrhUMyxrqscLtz9rYq9Pm9EStwutbna5zowZ7p7UnvmPDoBZYBdDgpaRBu5JqOTo3aeH5stqVJ7X9Buch0spdu0uRhoC9L+S/DDXkWhXlKBoWtR4F5HMltf7YXDsNHmzmC7OjdTQNnl1y9Aalwe3a+XqaBr1ySnCR7qsJNS76xvdqwmZmxceHzY7/wGEbsuYzTGFNJlhrxSujM25vDJsXpI6HHcaTrXnd9gzwL5HKpScEpsK8ofLJIGDazMn9uuz5LeoUCAStqPkdUQu79gPOVaxz29vQKya/YrPslygfcSZkkmPKRXSigipyrb8HdexsuR159wXFJNms/t5V5rvqP3Lo/Q8=&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://www.draw.io/js/viewer.min.js"></script>
</body>
</html>
