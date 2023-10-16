    STATISTICS FORMAT
____________________________________________________________________



1.1   File name
------------------


Each file is named using the format:

    delegated-extended

1.2   File format
-------------------

The file consists of: 

    - comments
    - file header lines
    - records

Header and record lines are structured as 'comma separated fields'
(CSV). Leading and trailing blank text in fields not meaningful.

The vertical line character '|' (ASCII code 0x7c) is used as the
CSV field separator.

After the header lines, records are not sorted.



1.2.1 Comments
----------------


Comments are denoted by # at the beginning of a line. No
line-embedded comments are permitted. Comments may occur at
any place in the file.

Example:

    #optional comments.
    #   any number of lines.

    #another optional comment.

Blank lines are permitted, and may occur at any place in the file.



1.2.2 File header
-------------------


The file header consists of the version line and the summary
lines for each type of record. 


Version line
------------

Format:

    version|registry|serial|records|startdate|enddate|UTCoffset

Where:

    version    format version number of this file, 
               currently 2.3;

    registry   as for records and filename (see below);

    serial     serial number of this file (within the
               creating RIR series);

    records    number of records in file, excluding blank
               lines, summary lines, the version line and 
               comments;

    startdate  start date of time period, in yyyymmdd 
               format;

    enddate    end date of period in yyyymmdd format;

    UTCoffset  offset from UTC (+/- hours) of local RIR
               producing file.



Summary line
------------

The summary lines count the number of record lines of each type in 
the file.

Format:

    registry|*|type|*|count|summary

Where:

    registry   as for records (see below);

    *          an ASCII '*' (unused field, retained for
               spreadsheet purposes);

    type       as for records (defined below);

    count      sum of the number of record lines of this 
               type in the file.

    summary    the ASCII string 'summary' (to distinguish 
               the record line);


Note that the count does not equate to the total amount of resources
for each class of record. This is to be computed from the records
themselves.



1.2.3 Records
---------------

After the defined file header, and excluding any space or comments,
each line in the file represents a single allocation (or assignment)
of a specific range of Internet number resources (IPv4, IPv6 or
ASN), made by the RIR identified in the record.

IPv4  records may represent non-CIDR ranges or CIDR blocks, and 
therefore the record format represents the beginning of range, and a
count. This can be converted to prefix/length using simple algorithms.

IPv6 records represent the prefix and the count of /128 instances 
under that prefix.

Format:

    registry|cc|type|start|value|date|status|opaque-id[|extensions...]

Where:

    registry   The registry from which the data is taken.

    cc         ISO 3166 2-letter code of the organisation to
               which the allocation or assignment was made. 
               May also include the following non-ISO 3166
               code: 

    type       Type of Internet number resource represented
               in this record. One value from the set of 
               defined strings:

                   {asn,ipv4,ipv6}

    start      In the case of records of type 'ipv4' or
               'ipv6' this is the IPv4 or IPv6 'first
               address' of the	range.

               In the case of an 16 bit AS number, the
               format is the integer value in the range:

                   0 - 65535

               In the case of a 32 bit ASN,  the value is
               in the range:

                   0 - 4294967296
  
               No distinction is drawn between 16 and 32
               bit ASN values in the range 0 to 65535.

    value      In the case of IPv4 address the count of
               hosts for this range. This count does not 
               have to represent a CIDR range.

               In the case of an IPv6 address the value 
               will be the CIDR prefix length from the 
               'first address'	value of <start>.

               In the case of records of type 'asn' the 
               number is the count of AS from this start 
               value.

    date       Date on this allocation/assignment was made
               by the RIR in the format:

                   YYYYMMDD

               Where the allocation or assignment has been
               transferred from another registry, this date
               represents the date of first assignment or
               allocation as received in from the original
               RIR.

               It is noted that where records do not show a 
               date of first assignment, this can take the 
               0000/00/00 value.

    status     Type of record from the set:

                   {available, allocated, assigned, reserved}

                   available    The resource has not been allocated
                                or assigned to any entity.

                   allocated    An allocation made by the registry 
                                producing the file.

                   assigned     An assignment made by the registry
                                producing the file.

                   reserved     The resource has not been allocated
                                or assigned to any entity, and is
                                not available for allocation or
                                assignment.

    opaque-id  This is an in-series identifier which uniquely
               identifies a single organisation, an Internet
               number resource holder.

               All records in the file with the same opaque-id
               are registered to the same resource holder.

               The opaque-id is not guaranteed to be constant
               between versions of the file.

               If the records are collated by type, opaque-id and
               date, records of the same type for the same opaque-id
               for the same date can be held to be a single
               assignment or allocation

    extensions In future, this may include extra data that
               is yet to be defined.



1.3   Historical resources
----------------------------


Early Registration Transfers (ERX) and legacy records do not
have any special tagging in the statistics reports. 


____________________________________________________________________