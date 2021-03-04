#What I want this to do:
#   I want this to copy all of the data in a given table,
#   then I want the old table to be deleted,
#   then I want a new table to be created with the new table headers,
#   and I want the data previously coppied to be put into the new table,
#   with a temporary value put in the new table headers
#
#   tempValForNewTableHeaders should be a list containing objects:
#       [{newTableHeader: valueForTableHeader},
#        {anotherNewTableHeader: anotherValueForTableHeader},
#       ...]

def migrate_table(tableName, oldTableHeaders, newTableHeaders, tempValForNewTableHeaders):
    return None
