class Characterisation(object):
    def __init__(char_self):
        
        import ipywidgets as wg
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict
        
        label_layout = wg.Layout(width="100pt")
        cbox_layout = wg.Layout(width="50pt")
        
        char_self.save_button = wg.Button(description="Save values")
        char_self.save_label = wg.Label(value="No values saved this session")
        
        
        def on_save_button_clicked(b):
            char_self.save_values()
        char_self.save_button.on_click(on_save_button_clicked)
        
        char_self.system_analysed = ["raw materials", "composite", "electrode",  "in-situ/ operando", "post mortem/ ex-situ"]

        char_self.techniques = {"Morphology": ["SEM", "SEM+EDX", "TEM", "TEM+EDX", "TEM diffraction", "Optical","XCT", "FIB+SEM"],
                      "Structure":  ["lab XRD", "lab XPS", "lab XRF", "NMR", "neutron", "XAS", "EXAFS", "SR XRD", "SR radiography", "SR XRF", "XANES"],
                      "Vibration": ["Raman", "FTIR", "UV-vis"],
                      "Electrode properties": ["4-point conductivity", "Other conductivity", "TGA", "DSC", "ICP-OES"],
                      "Area porosity": ["BET/ MBET", "DFT", "BJH", "HK", "Unspecified PSD"]}

        char_self.widgets = dict([(keys, dict([(technique_key, 
                                                dict([(component_key, wg.Checkbox(indent=False, value=False, layout=cbox_layout)) ## Modified to value=False 06/04/2025 to try to fix reloading issue!
                                                      for component_key in char_self.system_analysed]))
                                          for technique_key in values]))
                                     for keys, values in char_self.techniques.items()])

        char_self.accordion = wg.Accordion([
            wg.VBox([
                     wg.HBox([wg.Label(value="", layout=label_layout)]+\
                             [wg.Label(value=sys_name, layout=cbox_layout) for sys_name in char_self.system_analysed])]+
                     [wg.HBox([wg.Label(value=technique_keys, layout=label_layout)]+[*technique_values.values()]) 
                      for technique_keys, technique_values in values.items()]) 
            for keys, values in char_self.widgets.items()])
        
        char_self.vbox = wg.VBox([wg.HBox([char_self.save_button, char_self.save_label]),
                                  char_self.accordion])

        for title, (index, _) in zip([*char_self.widgets.keys()], enumerate(char_self.accordion.children)):
            char_self.accordion.set_title(index, "{}".format(title))
            
    def save_values(char_self, get_headings=False):
        ## To save characterisation data from accordion:
        techniques_bools = dict([(keys, 
                                  dict([(tech_name, 
                                        dict([(char_self.system_analysed[nname], tech_value.value) for 
                                              nname, tech_value in enumerate(values[tech_name].values())]))
                                   for tech_name in values.keys()]))
                                 for keys, values in char_self.widgets.items()])

        column_headings = [[[":".join((keys,
                   tech_keys,
                   sys_keys)) 
          for sys_keys in tech_values.keys()] 
          for tech_keys, tech_values in values.items()] for keys, values in techniques_bools.items()]

        technique_results = [[[*tech_values.values()] for tech_values in values.values()]\
                             for values in techniques_bools.values()]

        column_headings = [outer_item for outer_sublist in [item for sublist in column_headings for item in sublist]
                           for outer_item in outer_sublist]
        technique_results = [outer_item for outer_sublist in [item for sublist in technique_results for item in sublist]
                             for outer_item in outer_sublist]

        technique_dict = dict([(column_headings[n], [technique_results[n]]) for n in range(len(column_headings))])
        
        
        import pandas as pd
        df_techniques = (dict([("Characterisation_"+column_headings[n], [technique_results[n]]) for n in range(len(column_headings))]))
        
        if get_headings == False:
            from datetime import datetime
            char_self.save_label.value = "Data saved {}".format(datetime.now().strftime("%H:%M:%S"))
            return df_techniques
        elif get_headings == True:
            return [*dict(df_techniques).keys()]
        
    def reload_values(char_self, df, data_row):
        import numpy as np
#         print("Using hardcoded entries for test!")
#         df = pd.read_csv("Test characterisation.csv", index_col=0)
        characterisation_columns = [name.split("Characterisation_")[1] for name in df.columns if "Characterisation" in name]

        for name in characterisation_columns:
            category, technique, measurand = name.split(":")
            entry = df["Characterisation_"+name].iloc[data_row] ## may need different index when selected from dropdown
            
            ## Modified 06/04/2025 to try to enable reload
            if entry == True:            
                char_self.widgets[category][technique][measurand].value = bool(True)
            elif entry == False:
                char_self.widgets[category][technique][measurand].value = bool(False)
            else:
                char_self.widgets[category][technique][measurand].value = bool(False)