def template_json_task_output(*,
                              task_number: int,
                              task_desc: str,
                              function,
                              file_name: str | None = None
                              ) -> None:
    """Prints formatted output for each task."""

    print(f'Задание {task_number}: {task_desc}')
    if file_name is None:
        function()
    else:
        function(file_name)