import os.path
from typing import List
import dominate
from dominate.tags import *


class ReportBuilder:
    def __init__(self, artifacts_directory: str):
        self._artifacts_directory = artifacts_directory
        self._padding_multiplier = 20

    def create_report(self):
        doc = dominate.document(title='Report')

        with doc.head:
            meta(name="viewport", content="width=device-width, initial-scale=1")
            style(
                """\
                        .collapsible {
                            background-color: rgb(255, 255, 255);
                            color: white;
                            cursor: pointer;
                            padding: 0px;
                            width: 100%;
                            border: none;
                            text-align: left;
                            outline: none;
                            font-size: 18px;
                         }
                         
                        .failed {
                            background-color: rgb(120, 0, 0);
                        }

                        .passed {
                            background-color: rgb(0, 120, 0);
                        }

                        .active, .collapsible:hover {
                            background-color: rgb(255, 255, 255);
                        } 

                        .content {
                            padding: 0 0px;
                            display: none;
                            overflow: hidden;
                            background-color: white;
                        }
                     """
            )

        with doc:
            h2("Report")
            for test_result in self._tests_results:
                test_padding = test_result.nesting_level * self._padding_multiplier
                data_padding = test_padding + 10

                with button(type="button", class_="collapsible", style=f"padding-left: {test_padding}px"):
                    if test_result.success:
                        div(class_="passed").add(f"∟{test_result.name}")
                    else:
                        div(class_="failed").add(f"∟{test_result.name}")

                with div(class_="content"):
                    test_global_artifacts_path = test_result.artifacts_path
                    general_artifacts_path = self._artifacts_directory
                    test_local_artifacts_path = os.path.relpath(test_global_artifacts_path, general_artifacts_path)

                    artifacts = os.listdir(test_global_artifacts_path)
                    # Sort artifacts firstly by extension and then by file path
                    artifacts.sort(key=lambda f: f"{os.path.splitext(f)[1]}.{os.path.splitext(f)[0]}")

                    for file_name in artifacts:
                        file_path = os.path.join(test_global_artifacts_path, file_name)
                        file_local_path = os.path.join(test_local_artifacts_path, file_name)
                        # checking if it is a file and screenshot
                        if not os.path.isfile(file_path):
                            continue

                        with button(type="button", class_="collapsible", style=f"padding-left: {data_padding}px"):
                            div(style="background-color: rgb(211, 149, 35);").add(file_name)

                        with div(class_="content"):
                            if '.png' in file_name:
                                img(style=f"max-width: 500px; max-height: 500px; height: auto; padding-left: {data_padding}px;", src=f"{file_local_path}")
                            else:
                                a(href=file_local_path, target="_blank", rel="noopener noreferrer", style=f"padding-left: {data_padding}px",).add("show log...")

            script(
                '''\
                                    var coll = document.getElementsByClassName("collapsible");
                                    var i;
    
                                    for (i = 0; i < coll.length; i++) {
                                        coll[i].addEventListener("click", function() {
                                        this.classList.toggle("active");
                                        var content = this.nextElementSibling;
                                        if (content.style.display === "block") {
                                            content.style.display = "none";
                                        } else {
                                            content.style.display = "block";
                                        }
                                        });
                                    } 
                                '''
            )

        my_report = doc.render(pretty=True)
        my_readable_report = my_report.replace('&quot;', '"').replace('&lt;', '<').replace('class_', 'class')

        report_path = os.path.join(general_artifacts_path, 'report.html')
        with open(report_path, 'w') as report_file:
            report_file.write(my_readable_report)
