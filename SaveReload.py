class SaveReload(object):
    def __init__(save_self):
        from SelectFileButton import SelectFileGeneralButton
        import pandas as pd
        import ipywidgets as wg
        
        save_self.select_new_file_button = SelectFileGeneralButton(function='asksaveasfile')
        save_self.select_old_file_button = SelectFileGeneralButton(function='askopenfilename')
        save_self.confirm_save_location = wg.Button(description="Confirm file")
        save_self.choose_dropdown = wg.Dropdown(options=[""])
        save_self.confirm_dropdown = wg.Button(description="Confirm entry")
        
        save_self.save_label = wg.Label(value="No file selected")

        save_self.vbox = wg.VBox([wg.HBox([wg.Label("Start new data file"), save_self.select_new_file_button]),
                                    wg.HBox([wg.Label("Add to existing data file"), save_self.select_old_file_button]),
                                     wg.HBox([save_self.confirm_save_location, save_self.save_label]),
                                 wg.HBox([save_self.choose_dropdown, save_self.confirm_dropdown])])
        
    def on_confirm_save_location_clicked(save_self):
        print("Triggered SaveReload.on_confirm_save_location_clicked")
        import pandas as pd
        import numpy as np
                
        if len(save_self.select_new_file_button.files) > 0:
            save_self.save_path = save_self.select_new_file_button.files[0].name
            setattr(save_self, "_reload", False)
            save_self.save_label.value = "Saving new data to "+str(save_self.save_path)

        elif len(save_self.select_old_file_button.files) > 0:
            save_self.save_path = save_self.select_old_file_button.files[0]
            save_self.df_load = pd.read_csv(save_self.save_path, index_col=0)
            save_self.choose_dropdown.options = ["New entry"]+list(np.unique(save_self.df_load["concat_name"]))
            setattr(save_self, "_reload", True)
            save_self.save_label.value = "Reloading data from "+str(save_self.save_path)
            
    def on_confirm_dropdown_clicked(save_self, ): ## will need to move to outer
        save_self._target = save_self.choose_dropdown.value
#         if save_self._target != "New entry":
#         save_self.df = save_self.df_load
#             print("Loading only the line of the dataframe corresponding to the dropdown label!")
#             save_self.df = save_self.df_load.loc[save_self.df_load["concat_name"]==save_self._target]  