import csv, sys

'''HELPER FUNCTIONS'''
def read_cdx(filename):
    # Output:   Dictionary of cdx information
    # Format:   {document: [meta_data1, meta_data2, ..., meta_dataN]}
    #           meta_data = {'N', 'b', 'a', 'm', 's', 'k', 'r', 'M', 'V'}
    # Note:     This makes the output a dictionary in which each document
    #           contains a list of meta data dictionaries.
    #           To know how many mementos a document has, return the list
    #           length for that document
    cdx_dict = {}
    fieldnames = ['N', 'b', 'a', 'm', 's', 'k', 'r', 'M', 'V', 'g']
    with open(filename, 'r') as cdxfile:
        reader = csv.DictReader(cdxfile, fieldnames=fieldnames, delimiter=' ')
        reader.next()   # Skip header information
        for row in reader:
            orig_uri = row['a'] # Name of file being processed
            uri_metadata = {'N': row['N'], 'b': row['b'], 'm': row['m'], \
                            's': row['s'], 'k': row['k'], 'r': row['r'], \
                            'M': row['M'], 'V': row['V'], 'g': row['g']}
            #print doc_name
            #print doc_metadata
            try:
                cdx_dict[orig_uri].append(uri_metadata)
            except:
                if orig_uri[:3] != 'dns' and orig_uri != '-':
                    cdx_dict[orig_uri] = []
                    cdx_dict[orig_uri].append(uri_metadata)
        return cdx_dict

'''START SCRIPT'''
def main():
    num_arg = len(sys.argv)
    if num_arg < 2:
        print 'Usage: cdx_parser.py collection_id_1 collection_id_2 ... collection_id_n'
        return
    cdx_collections = sys.argv[1:]
    for collection in cdx_collections:
        print collection
        cdx_file = 'C:/_Kayla/phd_research/cdx_data/index-' + collection + '.cdx'
        cdx_dict = read_cdx(cdx_file)
        collection_uris = cdx_dict.keys()
        output_file = 'results/' + collection + '_count.csv'
        with open(output_file, 'w') as f:
            f.write('uri num_mementos\n')
            for uri in collection_uris:
                num_mementos = len(cdx_dict[uri])
                f.write('%s %d\n' % (uri, num_mementos))

if __name__ == "__main__":
    main()
