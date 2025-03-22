class ReportingChecklist(object):
    def __init__(report_self):
        
        import ipywidgets as wg
        import numpy as np
        import pandas as pd
        
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict

        
        report_self.save_button = wg.Button(description="Save values")
        report_self.save_label = wg.Label(value="No values saved this session")
        
########## Cell format ##########
        report_self.cell_format_widgets = {"Lithium anode":  wg.Checkbox(description="Lithium metal",indent=False),
                       "Graphite anode": wg.Checkbox(description="Graphite",indent=False),
                       "Silicon anode": wg.Checkbox(description="Silicon",indent=False),
                       "Other anode text": wg.Text(description="Other anode"),
                       "Sulfur": wg.Checkbox(description="Sulfur",indent=False),
                       "NMC811": wg.Checkbox(description="NMC811" ,indent=False),
                       "NMC622": wg.Checkbox(description="NMC622" ,indent=False),
                       "NMC532": wg.Checkbox(description="NMC532",indent=False),
                       "NMC111": wg.Checkbox(description="NMC111",indent=False),
                       "Other NMC": wg.Checkbox(description="Other NMC",indent=False),
                       "LFP": wg.Checkbox(description="LFP",indent=False),
                       "LFP/NMC blend": wg.Checkbox(description="LPF/NMC blend",indent=False),
                       "LCO": wg.Checkbox(description="LCO",indent=False),
                       "Other cathode text": wg.Text(description="Other cathode"),
                       "Cell format":  wg.Dropdown(description="Cell format",
                                                                      options=["Coin", "Swagelok", "Pouch", "Other"]),
                                          "Cell format other": wg.Text(description="Other"),
                                          "N/P electrode balance value":  wg.FloatText(description="N/P electrode balance"),
                                          "N/P reported": wg.Checkbox(description="Not reported", value=True),
                                          "N/P N/A": wg.Checkbox(description="N/A"),
                                          "Electrolyte volume reported": wg.FloatText(description="Electrolyte volume",
                                                                                      style={"description_width": "initial"}),
                                           "Electrolyte ratio reported": wg.FloatText(description="Electrolyte/ active ratio", 
                                                                                      style={"description_width": "initial"}),
                      }
        
        report_self.cell_format_vbox = wg.VBox([
          wg.VBox([wg.HBox([
    wg.VBox([wg.Label(value="Anode materials"), 
             report_self.cell_format_widgets["Lithium anode"],
             report_self.cell_format_widgets["Graphite anode"],
             report_self.cell_format_widgets["Silicon anode"],
             ]),
    wg.VBox([wg.Label(value="Cathode materials"),
             report_self.cell_format_widgets["Sulfur"],
             report_self.cell_format_widgets["NMC811"],
             report_self.cell_format_widgets["NMC622"],
             report_self.cell_format_widgets["NMC532"],
             report_self.cell_format_widgets["NMC111"],
             report_self.cell_format_widgets["Other NMC"],
             report_self.cell_format_widgets["LFP"],
             report_self.cell_format_widgets["LFP/NMC blend"],
             report_self.cell_format_widgets["LCO"]])
]),
         wg.HBox([report_self.cell_format_widgets["Other anode text"],
                  report_self.cell_format_widgets["Other cathode text"]])
         
         ]) ,
            wg.HBox([report_self.cell_format_widgets["Cell format"],
                                                         report_self.cell_format_widgets["Cell format other"]]),
                                                wg.HBox([report_self.cell_format_widgets["N/P electrode balance value"],
                                                         report_self.cell_format_widgets["N/P reported"],
                                                         report_self.cell_format_widgets["N/P N/A"]]),
                                                wg.HBox([report_self.cell_format_widgets["Electrolyte volume reported"],
                                                         report_self.cell_format_widgets["Electrolyte ratio reported"]])
        ])
        
########## Electrode processing ##########
        
        report_self.electrode_widgets = {"Assembly processing environment":  wg.Checkbox(description="Assembly/ processing environment", indent=False),
                                         "Production scale": wg.Checkbox(description="Production scale (g, kg...)", indent=False),
                                         "Production scale comment": wg.Text(description="Comment"),
                                         "Using commercial electrode": wg.RadioButtons(description="Using commercial electrode", options=["No", "Yes"], value="No"),
                                         "Electrode mass comp Binder": wg.Checkbox(description="Binder"),
                                         "Electrode mass comp Additive": wg.Checkbox(description="Additive"),
                                         "Electrode mass comp Active": wg.Checkbox(description="Active material"),
                                         "Electrode mass comp Solid content slurry": wg.Checkbox(description="Solid content slurry"),
                                         "Electrode thickness": wg.Text(description="Electrode thickness", style={"description_width": "initial"}),
                                         "Electrode how measured": wg.Dropdown(description="How measured",
                                                                               options=["", "Coating setting", "Calendering setting","Direct measurement","SEM","Inferred from mass"],
                                                           value=""),
                                         "Electrode mass loading": wg.Text(description="Electrode mass loading (total)", style={"description_width": "initial"}),
                                         "Calendered":wg.Checkbox(description="Calendared", indent=False),
                                         "Active material areal": wg.FloatText(description="Active material: Areal loading (mg/cm2)",
                                                           style={"description_width": "initial"}),
                                         "Active material fractional": wg.FloatText(description="Active material: Mass (wt%)",
                                                                style={"description_width": "initial"})}
        
        report_self.electrode_vbox = wg.VBox([report_self.electrode_widgets["Assembly processing environment"],
                                     wg.HBox([report_self.electrode_widgets["Production scale"], 
                                              report_self.electrode_widgets["Production scale comment"]]),
                                              report_self.electrode_widgets["Using commercial electrode"],
                                              wg.Label("Electrode composition reported"),
                                              report_self.electrode_widgets["Electrode mass comp Binder"],
                                              report_self.electrode_widgets["Electrode mass comp Additive"],
                                              report_self.electrode_widgets["Electrode mass comp Active"],
                                              report_self.electrode_widgets["Electrode mass comp Solid content slurry"],
                                              wg.HBox([report_self.electrode_widgets["Electrode thickness"], 
                                                       report_self.electrode_widgets["Electrode how measured"]]),
                                              report_self.electrode_widgets["Electrode mass loading"],
                                             report_self.electrode_widgets["Calendered"],
                                             report_self.electrode_widgets["Active material areal"],
                                             report_self.electrode_widgets["Active material fractional"]
                                    ])
        
########## Galvanostatic ##########

        report_self.galvanostatic_widgets = {"Voltage min": wg.FloatText(description="Min"),
                                             "Voltage max": wg.FloatText(description="Max"),
                                             "Different voltage range": wg.Checkbox(description="Multiple ranges", indent=False),
                                             "Voltage range NA" : wg.Checkbox(description="N/A", indent=False) ,
                                             "Pre-activation used": wg.Checkbox(description="Pre-activation used", indent=False),
                                             "Pre-activation rate": wg.FloatText(description="Rate"),
                                             "Pre-activation n cycles": wg.IntText(description="No. cycles"), 
                                             "Pre-activation other": wg.Text(description="Other"),
                                             "Pre-activation NA":wg.Checkbox(description="N/A"), 
                                             "C Rate min": wg.FloatText(description="Min"),
                                             "C Rate max": wg.FloatText(description="Max"), 
                                             "Current density min": wg.FloatText(description="Min"),
                                             "Current density max": wg.FloatText(description="Max"),
                                             "Current density report": wg.RadioButtons(options=["mA/mg", "mA/cm$^{2}$"]),
                                             "Constant voltage charge": wg.Checkbox(description="CV during charge", indent=False),
                                             "Constant voltage discharge": wg.Checkbox(description="CV during discharge", indent=False),
                                             "Multiple cells": wg.RadioButtons(description="Multiple cells shown with statistics?",
                                                                                options=["Yes (in article)", 
                                                                                         "Yes (In SI)", 
                                                                                         "No"], value="No"),
                                            }
    
    
        report_self.galvanostatic_vbox = wg.VBox([wg.Label("Galvanostatic cycling"),
                                                  wg.HBox([wg.Label("Galvanostatic voltage range"),
                                                           report_self.galvanostatic_widgets["Voltage min"],
                                                           report_self.galvanostatic_widgets["Voltage max"],
                                                           report_self.galvanostatic_widgets["Different voltage range"]]),
                                                  wg.HBox([report_self.galvanostatic_widgets["Pre-activation used"],
                                                           report_self.galvanostatic_widgets["Pre-activation rate"],
                                                           report_self.galvanostatic_widgets["Pre-activation n cycles"],
                                                           report_self.galvanostatic_widgets["Pre-activation other"],
                                                           report_self.galvanostatic_widgets["Pre-activation NA"]]),
                                                  wg.Label(value="C Rate"),
                                                  wg.HBox([
                                                            report_self.galvanostatic_widgets["C Rate min"],
                                                            report_self.galvanostatic_widgets["C Rate max"]
                                                           ]),
                                                  wg.Label(value="Current density"),
                                                  wg.HBox([
                                                            report_self.galvanostatic_widgets["Current density min"],
                                                            report_self.galvanostatic_widgets["Current density max"],
                                                            report_self.galvanostatic_widgets["Current density report"]
                                                           ]),
                                                  wg.Label(value="CC/CV (constant voltage)"),
                                                  wg.HBox([report_self.galvanostatic_widgets["Constant voltage charge"],
                                                           report_self.galvanostatic_widgets["Constant voltage discharge"]]),
                                                    report_self.galvanostatic_widgets["Multiple cells"],
                                            ])

        report_self.cv_widgets = {"Reported": wg.RadioButtons(description="CV reported?", options=["Yes", "No"], value=None),
                                  "Voltage min": wg.FloatText(description="Min"),
                                  "Voltage max": wg.FloatText(description="Max"), 
                                  "Sweep rate min": wg.FloatText(description="Min"),
                                  "Sweep rate max": wg.FloatText(description="Max"),
                                  "Linear scan current": wg.RadioButtons(description="Diffusion by Randles Sevcik eqn: demonstrated linear?",
                                            options=["Reported and checked",
                                                     "Reported, not checked",
                                                     "Not reported"], value="Not reported")}
        
        

        report_self.cv_vbox = wg.VBox([wg.Label(value="Cyclic voltammetry"),
                                         report_self.cv_widgets["Reported"], 
                        wg.HBox([wg.Label(value="Voltage range"),
                                report_self.cv_widgets["Voltage min"], report_self.cv_widgets["Voltage max"]]),
                            wg.HBox([wg.Label("Sweep/ scan rate"), 
                                     report_self.cv_widgets["Sweep rate min"], report_self.cv_widgets["Sweep rate max"]]),
                                       report_self.cv_widgets["Linear scan current"]
                            ])

        report_self.eis_widgets = {"Reported":  wg.RadioButtons(description="EIS reported?", options=["Yes", "No"], value=None),
               "ECM": wg.RadioButtons(description="Equivalent circuit model reported?", options=["None",
                                                                                        "2 component",
                                                                                        "3 component",
                                                                                        "4 component",
                                                                                        "5+ components"], value=None)}

        report_self.eis_vbox = wg.VBox([wg.Label(value="Electrochemical impedance spectroscopy"),
                     report_self.eis_widgets["Reported"],
                    report_self.eis_widgets["ECM"]
        ])
        
        report_self.test_params_widgets = {"Temperature": wg.RadioButtons(description="Temperature during electrochem testing",
                                                        options=["Not reported", 
                                                                 "Constant - non room temp",
                                                                 "Room temp",
                                                                 "Under test"]), 
                       "Theoretical capacity active material": wg.Checkbox(description="Active material", indent=False), 
                      "Theoretical capacity areal":  wg.Checkbox(description="Areal/ mass", indent=False),
                       "Theoretical capacity cell": wg.Checkbox(description="Cell", indent=False),
                                          "Theoretical capacity slow": wg.Checkbox(description="Slow initial/ formation")}
            

        report_self.electrochem_accordion = wg.Accordion([report_self.cell_format_vbox, 
                                              report_self.electrode_vbox,
                                              report_self.galvanostatic_vbox,
                                              report_self.cv_vbox,
                                              report_self.eis_vbox])
        for title, (index, _) in zip(["Cell format", "Electrode processing", "Galvanostatic", "CV", "EIS"],
                                     enumerate(report_self.electrochem_accordion.children)):
            report_self.electrochem_accordion.set_title(index, "{}".format(title))

        report_self.vbox = wg.VBox([wg.HBox([report_self.save_button, report_self.save_label]),
            report_self.test_params_widgets["Temperature"],
                                    wg.Label(value="Theoretical capacity calculated with respect to mass of..."),
                                  wg.HBox([report_self.test_params_widgets["Theoretical capacity active material"],
                                           report_self.test_params_widgets["Theoretical capacity areal"],
                                           report_self.test_params_widgets["Theoretical capacity cell"],
                                          report_self.test_params_widgets["Theoretical capacity slow"]]),
                                  report_self.electrochem_accordion
                                 ])
        
    def save_values(report_self, get_headings=False):
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict

        checklist_labels = {"test_params_widgets": "MeasurementCondition",
                             "cell_format_widgets": "CellFormat",
                             "electrode_widgets": "ElectrodeProcessing",
                             "galvanostatic_widgets": "Galvanostatic",
                             "cv_widgets": "CV",
                             "eis_widgets": "EIS"}

        checklist_savedict_multi = dict([(label, widgetdict_to_savedict(vars(report_self)[key], 
                                                                        label="Checklist"+label)) for key, label in checklist_labels.items()])
        df = {k: v for d in [*checklist_savedict_multi.values()] for k, v in d.items()}

        if get_headings == False:
            from datetime import datetime
            report_self.save_label.value = "Data saved {}".format(datetime.now().strftime("%H:%M:%S"))
            return df
        elif get_headings == True:
            return [*df.keys()]
        
    def reload(report_self, df, data_row):
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict

        checklist_labels = {"test_params_widgets": "MeasurementCondition",
                             "cell_format_widgets": "CellFormat",
                             "electrode_widgets": "ElectrodeProcessing",
                             "galvanostatic_widgets": "Galvanostatic",
                             "cv_widgets": "CV",
                             "eis_widgets": "EIS"}

        checklist_columns = [name for name in df.columns if "Checklist" in name]
#         data_row = 0

        reload_dict = {}

        for keys, values in checklist_labels.items():
            variable_columns = [name for name in df.columns if values in name]
            for variable in variable_columns:
                value_to_enter = df.loc[data_row, variable]
                if value_to_enter == True:
                    value_to_enter = bool(True)
                if value_to_enter == False:
                    value_to_enter = bool(False)

                try:
                    vars(report_self)[keys][variable.split("_")[1]].value = value_to_enter
                except:
                    pass
                
        print("Reporting reload runs OK")