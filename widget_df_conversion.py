def widgetdict_to_savedict(widgetdict, label, article=False):
    if article == False:
        return dict([(label+"_"+key,
                  [value.value]) for key, value in widgetdict.items()])
    if article == True:
        concat_name = " ".join((str(widgetdict[key].value) for key in ["First author", "Year", "Optional label"]))
        new_dict = dict([(label+"_"+key, [value.value]) for key, value in widgetdict.items()])
        new_dict.update([("concat_name", [concat_name])])
        return new_dict
    
    
def savedf_to_widgetdict(df, label, widgetdict, data_row):
    for keys, values in widgetdict.items():
        columns_labelled = [name for name in df.columns if label in name]
        col_header = [name for name in columns_labelled if name.split(label+"_")[1]==keys][0]
        value_to_write = df[col_header].iloc[data_row]
        if value_to_write == True:
            value_to_write = bool(True)
        elif value_to_write == False:
            value_to_write = bool(False)
            
        if "DOI" in keys:
            value_to_write = str(value_to_write)
#             print("TODO - make sure '/' and '_' save correctly")
        widgetdict[keys].value = value_to_write
        
    return widgetdict