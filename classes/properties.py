class Protein(object):
    """
    Parameters:
    ------
    Protein chain (String)

    Returns:
    ------
    The different properties of the protein

    ------
    * Stores length of the protein
    * Stores total amount of bindings
    * Stores total amount of polar aminoacids (P)
    * Stores total amount of hydrophobic aminoacids (H)
    * Stores total amount of Cysteines
    """

    def __init__(self, protein, length, total_p, total_h, total_c):
        """Initializer"""
        self.protein = protein
        self.length = length
        self.bindings = length - 1
        self.total_p = total_p
        self.total_h = total_h
        self.total_c = total_c

    def get_length(self, protein_string):
        """Gets a string containing the aminoacids of the protein.
        Returns an interger of the length of the protein."""
        length_protein = protein_string.len()
        return length_protein

    def get_bindings(self, length_protein):
        """ Gets a length from a protein. Returns the amount of covalent bonds it makes."""
        protein_bonds = length_protein - 1
        return protein_bonds

    def get_totals(self, protein_string):
        """ Gets a string containing H, P or C aminoacids and counts their amounts."""
        H_count = 0
        P_count = 0
        C_count = 0
        for element in protein_string:
            if element == 'H':
                H_count += 1
            elif element == 'P':
                P_count += 1
            elif element == 'C':
                C_count += 1
            else:
                return 1
