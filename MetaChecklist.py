class MetaChecklistTab(object):
    def __init__(self, test=False):
        import ipywidgets as wg
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd
        
        from SaveReload import SaveReload
        from Article import Article
        from ReportingChecklist import ReportingChecklist
        from Characterisation import Characterisation
        
        self._save_reload = SaveReload()
        self._article = Article()
        self._reports = ReportingChecklist()
        self._characterisation = Characterisation()
        
        
        def on_save_reload_confirm_clicked(b):
            print("Reload clicked")
            self._save_reload.on_confirm_save_location_clicked()
            self.save_path = self._save_reload.save_path
            
            print(self._save_reload.save_path)
            
            if self._save_reload._reload == False:
                self._article_headings = self._article.save_values(get_headings=True)
                self._report_headings = self._reports.save_values(get_headings=True)
                self._characterisation_headings = self._characterisation.save_values(get_headings=True)
                self._save_reload.confirm_dropdown.disabled = True
            
                self.df = pd.DataFrame(dict([(keys, [np.nan]) for keys in self._article_headings+self._report_headings+self._characterisation_headings]))
                self.df.to_csv(self.save_path)
                self._idx = 0
                print("Dataframe creating")
                
            elif self._save_reload._reload == True:
                print("Dataframe loading")
                self.df = pd.read_csv(self.save_path, index_col=0)
                
        def on_save_reload_dropdown_confirm_clicked(b):
            self._save_reload.on_confirm_dropdown_clicked()
            
            if self._save_reload._target != "New entry":
#                 self.df = self._save_reload.df
                self._idx = self.df.loc[self.df["concat_name"]==self._save_reload._target].index[0]

                self._article.reload_values(self.df, data_row=self._idx)
                self._reports.reload(self.df, data_row=self._idx)
                
                self._characterisation.reload_values(self.df, self._idx)
                
            elif self._save_reload._target == "New entry":
#                 self.df = self._save_reload.df
                self._idx = max(self.df.index)+1
                
            
        def on_article_save_clicked(b):
#             data_row = 0 ## to change to relevant row when dropdown selected            
            data_row = self._idx

            self.df = pd.read_csv(self.save_path, index_col=0)
            
            self.article_df = self._article.save_values()
            for keys, values in self.article_df.items():
                self.df.at[data_row, keys] = values[0]
                
            self.df.to_csv(self.save_path)
            
            
        def on_reporting_save_clicked(b):
            self.reporting_df = self._reports.save_values()
            
            data_row = self._idx
            self.df = pd.read_csv(self.save_path, index_col=0)
            for keys, values in self.reporting_df.items():
                self.df.at[data_row, keys] = values[0]
            self.df.to_csv(self.save_path)
            
        def on_characterisation_clicked(b):
            self.characterisation_df = self._characterisation.save_values()
            
            data_row = self._idx
            self.df = pd.read_csv(self.save_path, index_col=0)
            for keys, values in self.characterisation_df.items():
                self.df.at[data_row, keys] = values[0]
            self.df.to_csv(self.save_path)            
            
        self._save_reload.confirm_save_location.on_click(on_save_reload_confirm_clicked)
        self._save_reload.confirm_dropdown.on_click(on_save_reload_dropdown_confirm_clicked)
        self._article.save_button.on_click(on_article_save_clicked)
        self._reports.save_button.on_click(on_reporting_save_clicked)
        self._characterisation.save_button.on_click(on_characterisation_clicked)
        
        
        self.tab = wg.Tab([self._save_reload.vbox, 
                           self._article.vbox,
                           self._reports.vbox,
                           self._characterisation.vbox])
        
        for title, (index, _) in zip(["Save reload", "Article details", "Reporting checklist", "Characteriation"],
                                     enumerate(self.tab.children)):
            self.tab.set_title(index, "{}".format(title))        
            
        if test == True:
            self.save_path = "test_file_3.csv"
            self._article.widgets["First author"].value = "Darnielle"
            self._article.widgets["Year"].value = 2005
            self._article.widgets["Optional label"].value = "Champ"
            self._article.widgets["DOI"].value = "10.101010"
