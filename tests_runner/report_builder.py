import os.path
from typing import List
import dominate
from dominate.tags import *
from tests_runner.test_result_info import TestResultInfo


class ReportBuilder:
    def __init__(self, tests_results: List[TestResultInfo], artifacts_directory: str):
        self._tests_results = tests_results
        self._artifacts_directory = artifacts_directory
        self._padding_multiplier = 20

    def create_report(self):
        doc = dominate.document(title='Report')

        with doc.head:
            meta(name="viewport", content="width=device-width, initial-scale=1")
            style(
                """\
                        .collapsible {
                            background-color: rgb(200, 200, 200);
                            color: white;
                            cursor: pointer;
                            padding: 3px;
                            width: 100%;
                            border: none;
                            text-align: left;
                            outline: none;
                            font-size: 14px;
                         }
                         
                        .failed {
                            background-color: rgb(120, 0, 0);
                        }

                        .passed {
                            background-color: rgb(0, 120, 0);
                        }

                        .active, .collapsible:hover {
                            background-color: rgb(150, 150, 150);
                        } 

                        .content {
                            padding: 0 3px;
                            display: none;
                            overflow: hidden;
                            background-color: #f1f1f1;
                        }
                     """
            )

        with doc:
            h2("Report")
            for test_result in self._tests_results:
                with button(type="button", class_="collapsible", style=f"padding-left: {test_result.nesting_level * self._padding_multiplier}px"):
                    if test_result.success:
                        with div(class_="passed"):
                            div(f"∟{test_result.name}")
                    else:
                        with div(class_="failed"):
                            div(f"∟{test_result.name}")

                with div(class_="content"):
                    test_global_artifacts_path = test_result.artifacts_path
                    general_artifacts_path = self._artifacts_directory
                    test_local_artifacts_path = os.path.relpath(test_global_artifacts_path, general_artifacts_path)

                    for file_name in os.listdir(test_global_artifacts_path):
                        file_path = os.path.join(test_global_artifacts_path, file_name)
                        file_local_path = os.path.join(test_local_artifacts_path, file_name)
                        # checking if it is a file and screenshot
                        if os.path.isfile(file_path) and '.png' in file_name:
                            with button(type="button", class_="collapsible"):
                                div(file_name)
                            with div(class_="content"):
                                img(style="max-width: 500px; height: auto; ", src=f"{file_local_path}")

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
