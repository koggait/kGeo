    ASNAMES FORMAT
____________________________________________________________________

1.1   File name
------------------

Each version of this file is named using the format:

    asnames


1.2   File format
-------------------

The file consists of autonomous systems registration records.


1.2.3 Records
---------------

Each line in the file represents a single autonomous system number registration
of the Internet number resources made by one of the RIR.

Format:

    number name,cc

Where:

    number     AS number in the range of 0 - 4294967296

    name       The as name or the as name and organisation name of this as registrar.

    cc         ISO 3166 2-letter country codes to represent countries,
               dependent territories, and special areas of geographical interest.


1.3   Historical resources
----------------------------

Early Registration Transfers (ERX) and legacy records do not
have any special tagging in the this report.


____________________________________________________________________
written by Sebastian Kogga