class Protein(object):

    def __init__(self, protein, length, total_p, total_h, total_c):
        self.protein = protein
        self.length = length
        self.bindings = length - 1
        self.total_p = total_p
        self.total_h = total_h
        self.total_c = total_c

    def get_protein(self):
        pass

    def get_length(self):
        pass

    def get_bindings(self):
        pass

    def get_totals(self):
        pass
