import re
import requests

street_terms = ["alley", "allee", "allyaly", "annex", "anex", "annx", "anx", "arcade", "arc", "avenue", "av", "ave", "aven", "avenu", "avn", "avnue", "bayou", "bayoo", "byu", "beach", "bch", "bend", "bnd", "bluff", "bluf", "blf", "bluffs", "blfs", "bottom", "bot", "bottm", "btm", "boulevard", "boul", "boulv", "blvd", "branch", "brnch", "br", "bridge", "brdge", "brg", "brook", "brk", "brooks", "brks", "burg", "bg", "burgs", "bgs", "bypass", "bypa", "bypas", "byps", "byp", "camp", "cmp", "cp", "canyon", "canyn", "cnyn", "cyn", "cape", "cpe", "causeway", "causwa", "cswy", "center", "cen", "cent", "centr", "centre", "cnter", "cntr", "ctr", "centers", "ctrs", "circle", "circ", "circl", "crcl", "crcle", "cir", "circle", "cirs", "cliff", "clf", "cliffs", "clfs", "club", "clb", "common", "cmn", "commons", "cmns", "corner", "cor", "corners", "cors", "course", "crse", "court", "ct", "courts", "cts", "cove", "cv", "coves", "cvs", "creek", "crk", "crescent", "crsent", "crsnt", "cres", "crest", "crst", "crossing", "crssng", "xing", "crossroad", "xrd", "curve", "curv", "dale", "dl", "dam", "dm", "divide", "div", "dvd", "dv", "drive", "driv", "drv", "dr", "drives", "drs", "estate", "est", "estates", "ests", "expressway", "exp", "expr", "express", "expw", "expy", "extension", "extn", "extnsn", "ext", "extensions", "exts", "fallfalls", "fls", "ferry", "frry", "fry", "field", "fld", "fields", "flds", "flat", "flt", "flats", "flts", "ford", "frd", "fords", "frds", "forest", "frst", "forge", "forg", "frg", "forges", "frgs", "fork", "frk", "forks", "frks", "fort", "frt", "ft", "freeway", "freewy", "frway", "frwy", "fwy", "garden", "gardn", "grden", "grdn", "gdn", "gardens", "gdns", "gateway", "gatewy", "gatway", "gtway", "gtwy", "glen", "gln", "glens", "glns", "green", "grn", "greens", "grns", "grove", "grov", "grv", "groves", "grvs", "harb", "harb", "harbr", "hrb", "hbr", "harbors", "hbrs", "haven", "hvn", "heights", "hts", "highway", "highwy", "hiway", "hiwy", "hway", "hwy", "hill", "hl", "hills", "hls", "hollow", "hllw", "holw", "holws", "inlet", "inlt", "island", "is", "islands", "iss", "isle", "junction", "jction", "jctn", "junctn", "juncton", "jct", "junctions", "jcts", "key", "ky", "keys", "kys", "knoll", "knol", "knl", "knolls", "knls", "lake", "lk", "lakes", "lks", "landlanding", "lndng", "lndg", "lane", "ln", "light", "lgt", "lights", "lgts", "loaf", "lf", "lock", "lck", "locks", "lcks", "lodge", "ldge", "lodg", "ldg", "loopmallman", "mnr", "manors", "mnrs", "meadow", "mdw", "meadows", "medows", "mdws", "mewsmill", "ml", "mills", "mls", "mission", "msn", "motorway", "mtwy", "mount", "mt", "mountain", "mtn", "mountains", "mtns", "neck", "nck", "orchard", "orchrd", "orch", "oval", "ovl", "overpass", "opas", "park", "prk", "parks", "park", "parkway", "parkwy", "pkway", "pky", "pkwy", "parkways", "pkwys", "passpassage", "psge", "pathpikepine", "pne", "pines", "pnes", "place", "pl", "plain", "pln", "plains", "plns", "plaza", "plza", "plz", "point", "pt", "points", "pts", "port", "prt", "pors", "prts", "prairie", "prr", "pr", "radial", "rad", "radiel", "radl", "rampranch", "rnch", "rnchs", "rapid", "rpd", "rapids", "rpds", "rest", "rst", "ridge", "rdge", "rdg", "ridges", "rdgs", "river", "rvr", "rivr", "riv", "road", "rd", "roads", "rds", "route", "rte", "rowruerunshoal", "shl", "shoals", "shls", "shore", "shr", "shores", "shrs", "skyway", "skwy", "spring", "spng", "sprng", "spg", "springs", "spgs", "spursquare", "sqr", "sqre", "squ", "sq", "squares", "sqs", "station", "statn", "stn", "sta", "stravenue", "strav", "straven", "stravn", "strvn", "strvnue", "stra", "stream", "streme", "strm", "street", "str", "strt", "st", "streets", "sts", "summit", "sumit", "sumitt", "smt", "terrace", "terr", "ter", "throughway", "trwy", "trace", "trce", "track", "trak", "trk", "trks", "trafficway", "trfy", "trail", "trl", "trailer", "trlr", "tunnel", "tunl", "turnpike", "trnpk", "turnpk", "tpke", "underpass", "upas", "union", "un", "unions", "uns", "valley", "vally", "vlly", "vly", "valley", "vlys", "viaduct", "vdct", "viadct", "via", "view", "vw", "views", "vws", "village", "vill", "villag", "villg", "vlg", "villages", "vlgs", "ville", "vl", "vista", "vist", "vst", "vsta", "vis", "walkwallway", "wy", "well", "wl", "wells", "wls"]
street_terms_set = set(street_terms)

apt_terms = ["apartment", "ap", "apt", "basement", "box", "bsmt", "building", "bldg", "department", "dept", "floor", "fl", "front", "frnt", "hanger", "hngr", "key", "lobby", "lbby", "lot", "lower", "lowr", "no", "office", "ofc", "penthouse", "ph", "pier", "rear", "room", "rm", "side", "slip", "space", "spc", "stop", "suite", "ste", "trailer", "trlr", "unit", "upper", "uppr", "#"]
apt_terms_set = set(apt_terms)

sanitized_street_memo = {}

def shift_num(num):
    ''' Return a string
    if num < 10 make it 10
    if num % 10 == 0 add 5
    else get rid of the num at the unit's digit
    '''
    num = int(num)
    if (num < 10):
        num = 10
    elif (num % 10 == 0):
        num += 5
    else:
        num = num // 10 * 10
    return str(num)

def remove_num(addr):
    ''' Input address in string 
        Return a string
    if a number is concatenated with a string like xxxstr, leave the number since it is normally part of the street name. 
    However, if a number appears alone or concatenated after a string like strxxx, remove the number
    '''
    addr = re.sub(r'([a-zA-Z ]+)(\d+)(\W|\s|$)', r'\1', addr.strip())
    return addr.strip()

def has_street_term(addr):
   addr_arr = addr.split(' ')
   for addr_info in addr_arr:
       if (addr_info.lower() in street_terms_set):
           return True 
   return False

def remove_after_street_info(addr):
    if (addr in sanitized_street_memo.keys()):
        return sanitized_street_memo[addr]
    addr_arr = addr.split(' ')
    sanitized_street_memo[addr] = addr
    for addr_info in addr_arr:
        if (addr_info.lower() in street_terms_set):
            sanitized_addr = " ".join([addr.split(addr_info)[0].strip(), addr_info])
            sanitized_street_memo[addr] = sanitized_addr
            break
    
    return sanitized_street_memo[addr]

def has_apt_term(addr):
   addr_arr = addr.split(' ')
   for addr_info in addr_arr:
       if (addr_info.lower() in apt_terms_set):
           return True
   return False

def strip_apt_term(addr):
    ''' Input addresses in string
        Return a string
    '''
    if (addr in sanitized_street_memo.keys()):
        return sanitized_street_memo[addr]
    addr_arr = addr.split(' ')
    sanitized_street_memo[addr] = addr 
    for addr_info in addr_arr:
        if (addr_info.lower() in apt_terms_set):
            sanitized_addr = addr.split(addr_info)[0].strip()
            sanitized_street_memo[addr] = sanitized_addr
            break

    return sanitized_street_memo[addr]

def consume_api(api_endpoint, payload):
    resp = requests.post(api_endpoint, json=payload)
    if (resp.status_code != 200 and resp.status_code != 201):
        raise Exception('POST {} {}'.format(api_endpoint, resp.status_code))
    return resp.json()
