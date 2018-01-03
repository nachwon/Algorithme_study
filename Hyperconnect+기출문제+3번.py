class CategoryTree:
    def __init__(self):
        self.category_list = {}
    
    def add_category(self, category, parent=None):
        if parent is None:
            if category in self.category_list:
                raise KeyError(f"root category '{category}' already exists")
            self.category_list[category] = {}
        else:
            if parent not in self.category_list:
                raise KeyError(f"root category '{parent}' does not exist")
            self.category_list[parent].update({category: []})
            
    def get_children(self, parent):
        p_category = self.category_list[parent]
        
        if p_category is None:
            return f"category '{parent}' does not have any child category"
        else:
            return p_category.keys()


c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('A')))





