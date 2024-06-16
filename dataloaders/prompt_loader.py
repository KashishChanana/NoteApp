def _load_prompt(task_name:str):
        """
        Loads a prompt from a given file path.
        
        Args:
            file_path (str): Path to the prompt file.
        
        Returns:
            str: The content of the prompt file.
        """
        _prompt = {
             "KeyConceptsTask": "prompts/keywords.txt",
             "BlogTask": "prompts/blogformatter.txt",
             "SummaryTask": "prompts/summary.txt",
             "QATask":"prompts/qatask.txt"
        }
        try:
            print(task_name)
            file_path = _prompt.get(task_name)
            with open(file_path, 'r') as file:
                return file.read()
        except IOError as e:
            raise RuntimeError(f"Error reading prompt file {file_path}: {e}")
        
