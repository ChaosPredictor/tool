def ConfigSectionMap(this, section):
    dict1 = {}
    options = this.options(section)
    for option in options:
        try:
            dict1[option] = this.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
