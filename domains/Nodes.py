class Nodes:

    def __init__(
            self,
            parsing_node: str,
            parsing_name: str,
            parsing_smtng: str
            ):

        self.node = parsing_node
        self.name = parsing_name
        self.smthng = parsing_smtng

    def get_string_slurm(self):
        string_slurm_pattern = 'Name={:s} Node={:s} What={:s}'
        string_slurm = string_slurm_pattern.format(self.node, self.name, self.smthng)
        return string_slurm

    def to_string_gren(self):
        string_gren_pattern = 'Name={:s} Node={:s} What={:s}'
        string_gren = string_gren_pattern.format(self.node, self.name, self.smthng)
        return string_gren

    def update(self):
        pass