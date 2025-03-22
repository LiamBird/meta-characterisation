class Article(object):
    def __init__(article_self):
        import ipywidgets as wg
        import numpy as np
        
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict
        
        article_self.widgets = {"First author": wg.Text(description="First author"),
                   "Year": wg.IntText(description="Year"),
                   "Optional label": wg.Text(description="Optional label"),
                   "DOI": wg.Text(description="DOI")}

        article_self.save_button = wg.Button(description="Save values")
        article_self.save_label = wg.Label(value="No values saved this session")
        
        article_self.vbox = wg.VBox([wg.HBox([article_self.save_button,
                                              article_self.save_label]),
                                     article_self.widgets["First author"],
                                article_self.widgets["Year"],
                                article_self.widgets["Optional label"],
                                article_self.widgets["DOI"]])
        
    def save_values(article_self, get_headings=False):        
        import pandas as pd
        import os 
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict
        
        
        if get_headings == False:
            from datetime import datetime
            article_self.save_label.value = "Data saved {}".format(datetime.now().strftime("%H:%M:%S"))
            
            return widgetdict_to_savedict(article_self.widgets, label="Article", article=True)
            print("saved")   
            
            
        elif get_headings == True:
            empty_dict = widgetdict_to_savedict(article_self.widgets, label="Article", article=True)
            return [*empty_dict.keys()]
        
        
        
    def reload_values(article_self, df, data_row):
        from widget_df_conversion import widgetdict_to_savedict, savedf_to_widgetdict
        savedf_to_widgetdict(df, label="Article", widgetdict=article_self.widgets, data_row=data_row)
