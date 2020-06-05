# If you would like to add to this list, please let me know at alandgton@gmail.com
# Currently mayors and city council members and police commissioners

# a dictionary that maps states to dictionaries that map counties to contacts
# contacts are tuples (name, county, email)
mailing_list = {
    "Arizona" : {
        "Phoenix" : [
            ( "Mayor Kate Gallego", "Phoenix", "mayor.gallego@phoenix.gov"),
            ( "Vice Mayor Betty Guardado", "Phoenix", "council.district.5@phoenix.gov"),
            ( "Councilmember Thelda Williams", "Phoenix", "council.district.1@phoenix.gov"),
            ( "Councilman Jim Waring", "Phoenix", "council.district.2@phoenix.gov"),
            ( "Councilmember Debra Stark", "Phoenix", "council.district.3@phoenix.gov"),
            ( "Councilmember Laura Pastor", "Phoenix", "council.district.4@phoenix.gov"),
            ( "Councilmember Sal DiCiccio", "Phoenix", "council.district.6@phoenix.gov"),
            ( "Councilmember Michael Nowakowski", "Phoenix", "council.district.7@phoenix.gov"),
            ( "Councilmember Carlos Garcia", "Phoenix", "council.district.8@phoenix.gov"),
        ],
        "Tuscon" : [
            ( "Mayor Regina Romero", "Tuscon", "Mayor.Romero@tucsonaz.gov"),
            ( "Vice Mayor Steve Kozachik", "Tuscon", "ward6@tucsonaz.gov"),
            ( "Councilmember Lane Santa Cruz", "Tuscon", "ward1@tucsonaz.gov"),
            ( "Councilmember Paul Cunningham", "Tuscon", "ward2@tucsonaz.gov"),
            ( "Councilmember Paul Durham", "Tuscon", "ward3@tucsonaz.gov"),
            ( "Councilmember Nikki Lee", "Tuscon", "ward4@tucsonaz.gov"),
            ( "Councilmember Richard Fimbres", "Tuscon", "ward5@tucsonaz.gov"),
        ],
    },
    "California" : {
        "Alameda" : [
            ( "Mayor Marilyn Ezzy Ashcraft", "Alameda", "mezzyashcraft@alamedaca.gov"),
            ( "Vice Mayor John Knox White", "Alameda", "jknoxwhite@alamedaca.gov"),
            ( "Councilmember Tony Daysog", "Alameda", "tdaysog@alamedaca.gov"),
            ( "Councilmember Jim Oddie", "Alameda", "joddie@alamedaca.gov"),
            ( "Councilmember Malia Vella", "Alameda", "mvella@alamedaca.gov"),
            ( "District Attorney Nancy E. O’Malley", "Alameda", "info@alcoda.org"),
        ],
        "Bakersfield" : [
            ( "Mayor Karen Goh", "Bakersfield", "Mayor@bakersfieldcity.us"),
            ( "Councilmembers", "Bakersfield", "City_Council@bakersfieldcity.us"),
        ],
        "Fresno" : [
            ( "Mayor Lee Brand", "Fresno", "lee.brand@fresno.gov"),
            ( "Councilmember Esmeralda Soria", "Fresno", "esmeralda.soria@fresno.gov"),
            ( "Councilmember Miguel Arias", "Fresno", "miguel.arias@fresno.gov"),
            ( "Councilmember Paul Caprioglio", "Fresno", "paul.capriogolio@fresno.gov"),
            ( "Councilmember Luis Chavez", "Fresno", "luis.chavez@fresno.gov"),
            ( "Councilmember Garry Bredefeld", "Fresno", "garry.bredefeld@fresno.gov"),
            ( "Councilmember Nelson Esparza", "Fresno", "nelson.esparza@fresno.gov"),
            ( "City Manager Wilma Quan", "Fresno", "wilma.quan@fresno.gov"),
        ],
        "Los Angeles" : [
            ( "Mayor Eric Garcetti", "LA", "mayor.helpdesk@lacity.org" ),
            ( "City Attorney Mike Feuer", "LA", "mayor.garcetti@lacity.org" ),
            ( "Councilmember Nury Martinez", "LA", "councilmember.martinez@lacity.org"),
            ( "Councilmember Gil Cedillo", "LA", "councilmember.cedillo@lacity.org"),
            ( "Councilmember Paul Krekorian", "LA", "councilmember.Krekorian@lacity.org"),
            ( "Councilmember Bob Blumenfield", "LA", "councilmember.blumenfield@lacity.org"),
            ( "Councilmember David E. Ryu", "LA", "david.ryu@lacity.org"),
            ( "LA Board of Police Commissioners", "LA", "policecommission@lapd.online"),
        ],
        "Oakland" : [
            ( "Mayor Libby Schaaf", "Oakland", "officeofthemayor@oaklandnet.com"),
            ( "Ethics Commission", "Oakland", "ethicscommission@oaklandca.gov"),
            ( "Councilmember Dan Kalb", "Oakland", "dkalb@oaklandca.gov"),
            ( "Councilmember Rebecca Kaplan", "Oakland", "rkaplan@oaklandca.gov"),
            ( "Councilmember Nikki Fortunato Bas", "Oakland", "nfbas@oaklandca.gov"),
            ( "Councilmember Lynette Gibson McElhaney", "Oakland", "LMcElhaney@oaklandca.gov"),
            ( "Councilmember Sheng Thao", "Oakland", "district4@oaklandca.gov"),
            ( "Councilmember Loren Taylor", "Oakland", "District6@oaklandca.gov"),
            ( "Councilmember Noel Gallo", "Oakland", "Ngallo@oaklandca.gov"),
            ( "Councilmember Larry Reid", "Oakland", "lreid@oaklandnet.com"),
        ],
        "Orange County" : [
            ( "Supervisor Michelle Steel", "OC", "Michelle.Steel@ocgov.com"),
            ( "Supervisor Andrew Do", "OC", "Andrew.Do@ocgov.com"),
            ( "Supervisor Donald P. Wagner", "OC", "Donald.Wagner@ocgov.com"),
            ( "Supervisor Doug Chaffee", "OC", "Fourth.District@ocgov.com"),
            ( "Supervisor Lisa Bartlett", "OC", "Lisa.Bartlett@ocgov.com"),
            ( "Todd Spitzer", "OC", "media@da.ocgov.com"),
        ],
        "Sacramento" : [
            ( "Mayor Darrell Steinberg", "Sacramento", "MayorSteinberg@cityofsacramento.org"),
            ( "Vice Mayor Jeff Harris", "Sacramento", "jsharris@cityofsacramento.org"),
            ( "David Gonsalves", "Sacramento", "dgonsalves@cityofsacramento.org"),
            ( "Jocelyn Navarro", "Sacramento", "jonavarro@cityofsacramento.org"),
            ( "Councilmember Angelique Ashby", "Sacramento", "aashby@cityofsacramento.org"),
            ( "Councilmember Allen Wayne Warren", "Sacramento", "awarren@cityofsacramento.org"),
            ( "Councilmember Steve Hansen", "Sacramento", "SHansen@cityofsacramento.org"),
            ( "Councilmember Jay Schenirer", "Sacramento", "jschenirer@cityofsacramento.org"),
            ( "Councilmember Rick Jennings", "Sacramento", "rjennings@cityofsacramento.org"),
            ( "Councilmember Larry Carr", "Sacramento", "lcarr@cityofsacramento.org"),
            ( "Supervisor Phil Serna", "Sacramento", "SupervisorSerna@saccounty.net"),
            ( "Supervisor Patrick Kennedy", "Sacramento", "SupervisorKennedy@saccounty.net"),
            ( "Mayor Cabaldon", "West Sacramento", "christopherc@cityofwestsacramento.org"),
            ( "Councilmember Quirina Orozco", "West Sacramento", "quirinao@cityofwestsacramento.org"),
            ( "Councilmember Chris Ledesma", "West Sacramento", "chrisl@cityofwestsacramento.org"),
            ( "Councilmember Martha Guerrero", "West Sacramento", "mguerrero@cityofwestsacramento.org"),
            ( "Mayor Pro Tem Beverly Sandeen", "West Sacramento", "beverlys@cityofwestsacramento.org"),
        ],
        "San Diego" : [
            ( "Mayor Kevin Faulconer", "San Diego", "kevinfaulconer@sandiego.gov"),
            ( "Council President Barbara Bry", "San Diego", "barbarabry@sandiego.gov"),
            ( "Councilmember Jennifer Campbell", "San Diego", "jennifercampbell@sandiego.gov"),
            ( "Councilmember Chris Ward", "San Diego", "christopherward@sandiego.gov"),
            ( "Councilmember Monica Montgomery", "San Diego", "monicamontgomery@sandiego.gov"),
            ( "Councilmember Mark Kersey", "San Diego", "markkersey@sandiego.gov"),
            ( "Councilmember Chris Cate", "San Diego", "chriscate@sandiego.gov"),
            ( "Councilmember Scott Sherman", "San Diego", "scottsherman@sandiego.gov"),
            ( "Councilmember Vivian Moreno", "San Diego", "vivianmoreno@sandiego.gov"),
            ( "Councilmember Georgette Gomez", "San Diego", "georgettegomez@sandiego.gov"),
        ],
        "San Francisco" : [
            ( "Mayor London N. Breed", "SF", "MayorLondonBreed@sfgov.org"),
            ( "Supervisor Matt Haney", "SF", "Matt.Haney@sfgov.org"),
            ( "Supervisor Rafael Mandelman", "SF", "MandelmanStaff@sfgov.org"),
            ( "Supervisor Gordon Mar", "SF", "Gordon.Mar@sfgov.org"),
            ( "Supervisor Aaron Peskin", "SF", "Aaron.Peskin@sfgov.org"),
            ( "Supervisor Dean Preston", "SF", "Dean.Preston@sfgov.org"),
            ( "Supervisor Sandra Lee Fewer", "SF", "sandra.fewer@sfgov.org"),
            ( "Supervisor Hillary Ronen", "SF", "Hillary.Ronen@sfgov.org"),
            ( "Supervisor Ahsha Safai", "SF", "Ahsha.Safai@sfgov.org"),
            ( "Supervisor Catherine Stefani", "SF", "Catherine.Stefani@sfgov.org"),
            ( "Supervisor Shamann Walton", "SF", "Shamann.Walton@sfgov.org"),
            ( "Supervisor Norman Yee", "SF", "Norman.Yee@sfgov.org"),
            ( "San Francisco Police Commission", "SF", "sfpd.commission@sfgov.org"),
        ],
        "San Jose" : [
            ( "Mayor Sam Liccardo", "San Jose", "mayoremail@sanjoseca.gov"),
            ( "Vice Mayor Charles Jones", "San Jose", "District1@sanjoseca.gov"),
            ( "Councilmember Sergio Jimenez", "San Jose", "District2@sanjoseca.gov"),
            ( "Councilmember Raul Peralez", "San Jose", "District3@sanjoseca.gov"),
            ( "Councilmember Lan Diep", "San Jose", "District4@sanjoseca.gov"),
            ( "Councilmember Magdalena Carrasco", "San Jose", "District5@sanjoseca.gov"),
            ( "Councilmember Devora Davis", "San Jose", "District6@sanjoseca.gov"),
            ( "Councilmember Maya Esparza", "San Jose", "District7@sanjoseca.gov"),
            ( "Councilmember Sylvia Arenas", "San Jose", "District8@sanjoseca.gov"),
            ( "Councilmember Pam Foley", "San Jose", "District9@sanjoseca.gov"),
            ( "Councilmember Johnny Khamis", "San Jose", "District10@sanjoseca.gov"),
        ],
        "Santa Clara" : [
            ("Mayor Lisa Gillmore", "Santa Clara", "lgillmor@santaclaraca.gov"),
            ("Vice Mayor Karen Hardy", "Santa Clara", "khardy@santaclaraca.gov"),
            ("Councilmember Kathy Watanabe", "Santa Clara", "kwatanabe@santaclaraca.gov"),
            ("Councilmember Raj Chahal", "Santa Clara", "rchahal@santaclaraca.gov"),
            ("Councilmember Teresa O'Neill", "Santa Clara", "toneill@santaclaraca.gov"),
            ("Councilmember Karen Hardy", "Santa Clara", "khardy@santaclaraca.gov"),
            ("Councilmember Debbie Davis", "Santa Clara", "ddavis@santaclaraca.gov"),
            ("City Attorney Brian Doyle", "Santa Clara", "CityAttorney@santaclaraca.gov"),
        ],
    },
    "District of Columbia" : {
        "DC" : [
            ( "Mayor Muriel Bowser", "DC", "eom@dc.gov"),
            ( "Chairman Phil Mendelson", "DC", "pmendelson@dccouncil.us"),
            ( "Councilmember Kenyan McDuffie", "DC", "kmcduffie@dccouncil.us"),
            ( "Councilmember Anita Bonds", "DC", "abonds@dccouncil.us"),
            ( "Councilmember David Grosso", "DC", "dgrosso@dccouncil.us"),
            ( "Councilmember Robert White", "DC", "rwhite@dccouncil.us"),
            ( "Councilmember Elissa Silverman", "DC", "esilverman@dccouncil.us"),
            ( "Councilmember Brianne Nadeau", "DC", "bnadeau@dccouncil.us"),
            ( "Councilmember Mary Cheh", "DC", "mcheh@dccouncil.us"),
            ( "Councilmember Brandon Todd", "DC", "btodd@dccouncil.us"),
            ( "Councilmember Charles Allen", "DC", "callen@dccouncil.us"),
            ( "Councilmember Vincent Gray", "DC", "vgray@dccouncil.us"),
            ( "Councilmember Trayon White", "DC", "twhite@dccouncil.us"),
        ],
    },
    "Georgia" : {
        "Atlanta" : [
            ("Mayor Keisha Lance Bottoms", "Atlanta", "kbottoms@atlantaga.gov"),
            ("Council President Felicia A. Moore", "Atlanta", "fmoore@atlantaga.gov"),
            ("Councilmember Carla Smith", "Atlanta", "csmith@atlantaga.gov"),
            ("Councilmember Amir R. Farokhi", "Atlanta", "arfarokhi@atlantaga.gov"),
            ("Councilmember Antonio Brown", "Atlanta", "antoniobrown@atlantaga.gov"),
            ("Councilmember Cleta Winslow", "Atlanta", "cwinslow@atlantaga.gov"),
            ("Councilmember Natalyn Archibong", "Atlanta", "narchibong@atlantaga.gov"),
            ("Councilmember Jennifer N. Ide", "Atlanta", "jnide@atlantaga.gov"),
            ("Councilmember Howard Shook", "Atlanta", "hshook@atlantaga.gov"),
            ("Councilmember J.P. Matzigkeit", "Atlanta", "jpmatzigkeit@atlantaga.gov"),
            ("Councilmember Dustin Hills", "Atlanta", "drhillis@atlantaga.gov"),
            ("Councilmember Andrea L. Boone", "Atlanta", "aboone@atlantaga.gov"),
            ("Councilmember Marci Collier Overstreet", "Atlanta", "mcoverstreet@atlantaga.gov"),
            ("Councilmember Joyce Sheperd", "Atlanta", "jmsheperd@atlantaga.gov"),
            ("Councilmember Michael Julian Bond", "Atlanta", "mbond@atlantaga.gov"),
            ("Councilmember Matt Westmoreland", "Atlanta", "mwestmoreland@atlantaga.gov"),
            ("Councilmember Andre Dickens", "Atlanta", "adickens@atlantaga.gov"),
        ],
    },
    "Illinois" : {
        "Chicago" : [
            ("Mayor Lori Lightfoot", "Chicago", "letterforthemayor@cityofchicago.org"),
        ],
    },
    "Massachusetts" : {
        "Boston" : [
            ( "Mayor Martin Walsh", "Boston", "mayor@boston.gov"),
            ( "Councilmember Annissa Essaibi George", "Boston", "A.E.George@boston.gov"),
            ( "Councilmember Michael Flaherty", "Boston", "Michael.F.Flaherty@boston.gov"),
            ( "Councilmember Michelle Wu", "Boston", "Michelle.Wu@boston.gov"),
            ( "Councilmember Lydia Edwards", "Boston", "lydia.edwards@boston.gov"),
            ( "Councilmember Ed Flynn", "Boston", "ed.flynn@boston.gov"),
            ( "Councilmember Frank Baker", "Boston", "Frank.Baker@boston.gov"),
            ( "Councilmember Andrea Campbell", "Boston", "Andrea.Campbell@boston.gov"),
            ( "Councilmember Ricardo Arroyo", "Boston", "ricardo.arroyo@boston.gov"),
            ( "Councilmember Matt O'Malley", "Boston", "matthew.omalley@boston.gov"),
            ( "Councilmember Kenzie Bok", "Boston", "kenzie.bok@boston.gov"),
            ( "Commissioner William Gross", "Boston", "mediarelations@pd.boston.gov"),
        ],
    },
    "Minnesota" : {
        "Minneapolis" : [
            ( "Mayor Jacob Frey", "Minneapolis", "Jacob.Frey@minneapolismn.gov"),
            ( "Councilmember Kevin Reich", "Minneapolis", "kevin.reich@minneapolismn.gov"),
            ( "Councilmember Cam Gordon", "Minneapolis", "cam.gordon@minneapolismn.gov"),
            ( "Councilmember Steve Fletcher", "Minneapolis", "steve.fletcher@minneapolismn.gov"),
            ( "Councilmember Phillipe Cunningham", "Minneapolis", "Phillipe.Cunningham@minneapolismn.gov"),
            ( "Councilmember Jeremiah Ellison", "Minneapolis", "Jeremiah.Ellison@minneapolismn.gov"),
            ( "Councilmember Lisa Goodman", "Minneapolis", "Lisa.Goodman@minneapolismn.gov"),
            ( "Councilmember Andrea Jenkins", "Minneapolis", "Andrea.Jenkins@minneapolismn.gov"),
            ( "Councilmember Alondra Cano", "Minneapolis", "Alondra.Cano@minneapolismn.gov"),
            ( "Councilmember Lisa Bender", "Minneapolis", "Lisa.Bender@minneapolismn.gov"),
            ( "Councilmember Jeremy Schroeder", "Minneapolis", "Jeremy.Schroeder@minneapolismn.gov"),
            ( "Councilmember Andrew Johnson", "Minneapolis", "Andrew.Johnson@minneapolismn.gov"),
            ( "Councilmember Linea Palmisano", "Minneapolis", "Linea.Palmisano@minneapolismn.gov"),
        ],
    },
    "Missouri" : {
        "Greene County" : [
            ( "Representative Sonya Anderson", "Greene County", "Sonya.Anderson@house.mo.gov"),
            ( "Representative Jeffrey Messenger", "Greene County", "Jeff.Messenger@house.mo.gov"),
        ],
        "Jefferson County" : [
            ( "Representative Rob Vescovo", "Jefferson County", "Rob.Vescovo@house.mo.gov"),
        ],
        "Kansas City" : [
            ( "Representative Keri Ingle", "Kansas City", "Keri.Ingle@house.mo.gov"),
            ( "Representative Ingrid Burnett", "Kansas City", "Ingrid.Burnett@house.mo.gov"),
            ( "Representative Barbara Washington", "Kansas City", "Barbara.Washington@house.mo.gov"),
        ],
        "Pulaski County" : [
            ( "Representative Steve Lynch", "Pulaski County", "Steve.Lynch@house.mo.gov"),
        ],
        "Springfield" : [
            ( "Representative Crystal Quade", "Springfield", "Crystal.Quade@house.mo.gov"),
            ( "Representative Elijah Haah", "Springfield", "Elijah.Haahr@house.mo.gov"),
        ],
        "St. Charles County" : [
            ( "Representative John Wiemann", "St. Charles County", "John.Wiemann@house.mo.gov"),
        ],
        "St. Louis County" : [
            ( "Mayor Lyda Krewson", "St. Louis", "krewsonl@stlouis-mo.gov"),
            ( "Senator Jill Schupp", "St. Louis", "jill.schupp@senate.mo.gov"),
            ( "Representative Tracy McCreery", "St. Louis", "Tracy.McCreery@house.mo.gov"),
            ( "Representative Tommie Pierson", "St. Louis", "Tommie.PiersonJr@house.mo.gov"),
            ( "Representative Kevin Windham", "St. Louis", "Kevin.Windhamjr@house.mo.gov"),
            ( "Representative Sarah Unsicker", "St. Louis", "Sarah.Unsicker@house.mo.gov"),
        ],
        "Daviess, DeKalb, Gentry, and Harrison Counties" : [
            ( "Representative J. Eggleston", "Missouri", "J.Eggleston@house.mo.gov"),
        ],
        "Washington, Wayne, Reynolds, and Iron Counties" : [
            ( "Representative Chris Dinkins", "Missouri", "Chris.Dinkins@house.mo.gov"),
        ],
    },
    "Nevada" : {
        "Las Vegas" : [
            ( "Mayor Carolyn Goodman", "Las Vegas", "cgoodman@lasvegasnevada.gov"),
            ( "Councilman Brian Knudsen", "Las Vegas", "ward1@lasvegasnevada.gov"),
            ( "Councilwoman Victoria Seaman", "Las Vegas", "ward2@lasvegasnevada.gov"),
            ( "Councilwoman Olivia Diaz", "Las Vegas", "ward3@lasvegasnevada.gov"),
            ( "Councilman Stavros S. Anthony", "Las Vegas", "ward4newsletter@lasvegasnevada.gov"),
            ( "Councilman Cedric Crear", "Las Vegas", "ccrear@lasvegasnevada.gov"),
            ( "Councilwoman Michele Fiore", "Las Vegas", "mfiore@lasvegasnevada.gov"),
            ( "City Manager Scott D. Adams", "Las Vegas", "sadams@lasvegasnevada.gov"),
        ],
        "Reno" : [
            ( "Mayor Hillary Schieve", "Reno", "mayor@reno.gov"),
            ( "Rick Caldeira", "Reno", "caldeirar@reno.gov"),
            ( "Councilmember Devon Reese", "Reno", "reesed@reno.gov"),
            ( "Councilmember Jenny Brekhus", "Reno", "brekhusj@reno.gov"),
            ( "Councilmember Naomi Duerr", "Reno", "duerrn@reno.gov"),
            ( "Councilmember Oscar Delgado", "Reno", "delgadoo@reno.gov"),
            ( "Councilmember Bonnie Weber", "Reno", "weberb@reno.gov"),
            ( "Councilmember Neoma Jardon", "Reno", "jardonn@reno.gov"),
        ],
    },
    "New York" : {
        "NYC" : [
            ( "Mayor Bill de Blasio", "NYC", "bdeblasio@cityhall.nyc.gov"),
            ( "Manhattan Borough President Gale Brewer", "NYC", "gbrewer@manhattanbp.nyc.gov"),
            ( "Director Jeremy Unger", "NYC", "junger@council.nyc.gov"),
            ( "Councilperson Corey Johnson", "NYC", "SpeakerJohnson@council.nyc.gov"),
            ( "Councilperson Keith Powers", "NYC", "kpowers@council.nyc.gov"),
            ( "Senator Brad Hoylman", "NYC", "hoylman@nysenate.gov"),
            ( "Senator Brian Kavanaugh", "NYC", "kavanagh@nysenate.gov"),
            ( "Assemblymember Richard Gottfried", "NYC", "GottfriedR@assembly.state.ny.us"),
            ( "Assemblymember Deborah Glick", "NYC", "glickd@assembly.state.ny.us"),
        ],
    },
    "North Carolina" : {
        "Durham County" : [
            ( "Chair Wendy Jacobs", "Durham County", "wjacobs@dconc.gov" ),
            ( "Vice-Chairman James Hill", "Durham County", "jahill@dconc.gov" ),
            ( "Commissioner Heidi Carter", "Durham County", "hcarter@dconc.gov" ),
            ( "Commissioner Brenda Howerton", "Durham County", "bhowerton@dconc.gov" ),
            ( "Commissioner Ellen Reckhow", "Durham County", "ereckhow@dconc.gov" ),
            ( "Sheriff Clarence Birkhead", "Durham County", "sheriffbirkhead@durhamsheriff.org" ),
        ],
        "Wake County" : [
            ( "Commissioner Sig Hutchinson", "Wake County", "Sig.Hutchinson@wakegov.com" ),
            ( "Commissioner Matt Calabria", "Wake County", "Matt.Calabria@wakegov.com" ),
            ( "Commissioner Susan Evans", "Wake County", "Susan.Evans@wakegov.com" ),
            ( "Commissioner Jessica Holmes", "Wake County", "Jessica.Holmes@wakegov.com" ),
            ( "Commissioner James West", "Wake County", "james.west@wakegov.com" ),
            ( "Chairman Greg Ford", "Wake County", "Greg.Ford@wakegov.com" ),
            ( "Vice-Chair Vickie Adamson", "Wake County", "Vickie.Adamson@wakegov.com" ),
            ( "County Manager David Ellis", "Wake County", "David.Ellis@wakegov.com" ),
            ( "Sheriff Gerald Baker", "Wake County", "gerald.baker@wakegov.com" ),
        ],
        "Durham" : [
            ( "Councilwoman Javiera Caballero", "Durham", "Javiera.Caballero@durhamnc.gov" ),
            ( "Councilwoman DeDreana Freeman", "Durham", "dedreana.freeman@durhamnc.gov" ),
            ( "Councilman Mark-Anthony Middleton", "Durham", "Mark-Anthony.Middleton@durhamnc.gov" ),
            ( "Mayor Pro Tempore Jillian Johnson", "Durham", "Jillian.Johnson@durhamnc.gov" ),
            ( "Councilman Charlie Reece", "Durham", "charlie.reece@durhamnc.gov" ),
            ( "Mayor Steve Schewel", "Durham", "Steve.Schewel@durhamnc.gov" ),
            ( "Chief CJ Davis", "Durham", "policechief@durhamnc.gov" ),
        ],
        "Raleigh" : [
            ( "City Manager Ruffin Hall", "Raleigh", "citymanager@raleighnc.gov" ),
            ( "Chief Cassandra Deck-Brown", "Raleigh", "cassandra.deck-brown@raleighnc.gov" ),
            ( "Mayor Mary-Ann Baldwin", "Raleigh", "mary-ann.baldwin@raleighnc.gov" ),
            ( "Councilman Jonathan Melton", "Raleigh", "jonathan.melton@raleighnc.gov" ),
            ( "Councilwoman Nicole Stewart", "Raleigh", "nicole.stewart@raleighnc.gov" ),
            ( "Councilman Patrick Buffkin", "Raleigh", "patrick.buffkin@raleighnc.gov" ),
            ( "Councilman David Cox", "Raleigh", "david.cox@raleighnc.gov" ),
            ( "Councilman Corey Branch", "Raleigh", "corey.branch@raleighnc.gov" ),
            ( "Councilman Saige Martin", "Raleigh", "saige.martin@raleighnc.gov" ),
            ( "Councilman David Knight", "Raleigh", "david.knight@raleighnc.gov" ),
        ],
        "Apex" : [
            ( "Mayor Jacques Gilbert", "Apex", "jacques.gilbert@apexnc.org" ),
            ( "Mayor Pro Tem Nicole Dozier", "Apex", "nicole.dozier@apexnc.org" ),
            ( "Council Member Brett Gantt", "Apex", "brett.gantt@apexnc.org" ),
            ( "Council Member Audra Killingsworth", "Apex", "audra.killingsworth@apexnc.org" ),
            ( "Council Member Terry Mahaffey", "Apex", "terry.mahaffey@apexnc.org" ),
            ( "Council Member Cheryl Stallings", "Apex", "cheryl.stallings@apexnc.org" ),
            ( "Chief John Letteney", "Apex", "John.Letteney@apexnc.org" ),
        ],
        "Cary" : [
            ( "Chief Toni Dezomits", "Cary", "toni.dezomits@townofcary.org" ),
            ( "Councilman Jack Smith", "Cary", "jack.smith@townofcary.org" ),
            ( "Councilman Ed Yerha", "Cary", "ed.yerha@townofcary.org" ),
            ( "Councilwoman Ya Liu", "Cary", "ya.liu@townofcary.org" ),
            ( "Mayor Harold Weinbrecht", "Cary", "harold.weinbrecht@townofcary.org" ),
            ( "Councilwoman Jennifer Robinson", "Cary", "jennifer.robinson@townofcary.org" ),
            ( "Mayor Pro Tem Don Frantz", "Cary", "don.frantz@townofcary.org" ),
            ( "Councilwoman Lori Bush", "Cary", "lori.bush@townofcary.org" ),
        ],
        "Fuquay-Varina" : [
            ( "Town Manager Adam Mitchell", "Fuquay-Varina", "amitchell@fuquay-varina.org" ),
            ( "Mayor John Byrne", "Fuquay-Varina", "jbyrne@fuquay-varina.org" ),
            ( "Mayor Pro Tem Blake Massengill", "Fuquay-Varina", "bmassengill@fuquay-varina.org" ),
            ( "Commissioner Marilyn Gardner", "Fuquay-Varina", "mgardner@fuquay-varina.org" ),
            ( "Commissioner William Harris", "Fuquay-Varina", "wharris@fuquay-varina.org" ),
            ( "Commissioner Larry Smith", "Fuquay-Varina", "lsmith@fuquay-varina.org" ),
            ( "Commissioner Jason Wunsch", "Fuquay-Varina", "jwunsch@fuquay-varina.org" ),
            ( "Chief Laura Fahnestock", "Fuquay-Varina", "lfahnestock@fuquay-varina.org" ),
        ],
    },
    "Oregon" : {
        "Portland" : [
            ( "Mayor Ted Wheeler", "Portland", "mayorwheeler@portlandoregon.gov"),
            ( "Commissioner Amanda Fritz", "Portland", "Amanda@portlandoregon.gov"),
            ( "Commissioner Jo Ann Hardesty", "Portland", "JoAnn@portlandoregon.gov"),
            ( "Commissioner Nick Fish", "Portland", "nick@portlandoregon.gov"),
            ( "Commissioner Chloe Eudaly", "Portland", "chloe@portlandoregon.gov"),
        ],
    },
    "Pennsylvania" : {
        "Philadelphia" : [
            ( "Mayor Jim Kenney", "Philadelphia", "james.kenney@phila.gov"),
            ( "Council President Darrell Clarke", "Philadelphia", "darrell.clarke@phila.gov"),
            ( "Councilmember Mark Squilla", "Philadelphia", "mark.squilla@phila.gov"),
            ( "Councilmember Kenyatta Johnson", "Philadelphia", "kenyatta.johnson@phila.gov"),
            ( "Councilmember Jamie Gauthier", "Philadelphia", "jamie.gauthier@phila.gov"),
            ( "Councilmember Curtis Jones", "Philadelphia", "curtis.jones@phila.gov"),
            ( "Councilmember Bobby Henon", "Philadelphia", "bobby@bobbyhenon.com"),
            ( "Councilmember Maria Quiñones Sánchez", "Philadelphia", "maria.q.sanchez@phila.gov"),
            ( "Councilmember Cindy Bass", "Philadelphia", "cindy.bass@phila.gov"),
            ( "Councilmember Cherelle Parker", "Philadelphia", "cherelle.parker@phila.gov"),
            ( "Councilmember Brian O'Neill", "Philadelphia", "brian.o'neill@phila.gov"),
            ( "Councilmember Kendra Brooks", "Philadelphia", "Kendra.Brooks@phila.gov"),
            ( "Councilmember Allan Domb", "Philadelphia", "allan.domb@phila.gov"),
            ( "Councilmember Derek Green", "Philadelphia", "derek.green@phila.gov"),
            ( "Councilmember Helen Gym", "Philadelphia", "helen.gym@phila.gov"),
            ( "Councilmember David Oh", "Philadelphia", "david.oh@phila.gov"),
            ( "Councilmember Isaiah Thomas", "Philadelphia", "Isaiah.Thomas@phila.gov"),
            ( "Commissioner Richard Ross", "Philadelphia", "police.commissioner@phila.gov"),
        ],
    },
    "Texas" : {
        "Austin" : [
            ( "Mayor Steve Adler", "Austin", "steve.adler@austintexas.gov"),
        ],
        "Dallas" : [
            ( "Mayor Pro Tem Adam Medrano", "Dallas", "adam.medrano@dallascityhall.com"),
            ( "Deputy Mayor Pro Tem B. Adam McGough", "Dallas", "adam.mcgough@dallascityhall.com"),
            ( "Council Liaison Laura Cadena", "Dallas", "Laura.Cadena@dallascityhall.com"),
            ( "Council Assistant Yesenia Valdez", "Dallas", "Yesenia.Valdez@dallascityhall.com"),
            ( "Councilmember Chad West", "Dallas", "Chad.West@dallascityhall.com"),
            ( "Councilmember Casey Thomas, II", "Dallas", "richard.soto@dallascityhall.com"),
            ( "Councilmember Carolyn King Arnold", "Dallas", "District4@DallasCityHall.com"),
            ( "Councilmember Jaime Resendez", "Dallas", "jaime.resendez@dallascityhall.com"),
            ( "Councilmember Tennell Atkins", "Dallas", "maria.salazar2@dallascityhall.com"),
            ( "Councilmember Paula Blackmon", "Dallas", "District9@DallasCityHall.com"),
            ( "Councilmember Lee M. Kleinman", "Dallas", "sophia.figueroa@dallascityhall.com"),
            ( "Councilmember Cara Mendelsohn", "Dallas", "cara.mendelsohn@dallascityhall.com"),
        ],
        "Houston" : [
            ( "Mayor Sylvester Turner", "Houston", "mayor@houstontx.gov"),
            ( "Councilmember Amy Peck", "Houston", "districta@houstontx.gov"),
            ( "Councilmember Jerry Davis", "Houston", "districtb@houstontx.gov"),
            ( "Councilmember Abbie Kamin", "Houston", "districtc@houstontx.gov"),
            ( "Councilmember Carolyn Evans-Shabazz", "Houston", "districtd@houstontx.gov"),
            ( "Councilmember Dave Martin", "Houston", "districte@houstontx.gov"),
            ( "Councilmember Tiffany Thomas", "Houston", "districtf@houstontx.gov"),
            ( "Councilmember Greg Travis", "Houston", "districtg@houstontx.gov"),
            ( "Councilmember Karla Cisneros", "Houston", "districth@houstontx.gov"),
            ( "Councilmember Robert Gallegos", "Houston", "districti@houstontx.gov"),
            ( "Councilmember Edward Pollard", "Houston", "districtj@houstontx.gov"),
            ( "Councilmember Martha Castex-Tatum", "Houston", "districtk@houstontx.gov"),
        ],
        "Plano" : [
            ( "Mayor Harry LaRosiliere", "Plano", "mayor@plano.gov"),
            ( "Mayor Pro Tem Kayci Prince", "Plano", "kayciprince@plano.gov"),
            ( "Deputy Mayor Pro Tem Anthony Ricciardelli", "Plano", "aricciardelli@plano.gov"),
            ( "Councilmember Maria Tu", "Plano", "mariatu@plano.gov"),
            ( "Councilmember Rick Grady", "Plano", "rickgrady@plano.gov"),
            ( "Councilmember Shelby Williams", "Plano", "shelbywilliams@plano.gov"),
            ( "Councilmember Rick Smith", "Plano", "ricksmith@plano.gov"),
            ( "Councilmember Lily Bao", "Plano", "lilybao@plano.gov"),
        ],
    },
    "Washington" : {
        "Seattle" : [
            ( "Mayor Jenny Durkan", "Seattle", "jenny.durkan@seattle.gov"),
            ( "Councilmember Lisa Herbold", "Seattle", "lisa.herbold@seattle.gov"),
            ( "Councilmember Tammy Morales", "Seattle", "tammy.morales@seattle.gov"),
            ( "Councilmember Kshama Sawant", "Seattle", "kshama.sawant@seattle.gov"),
            ( "Councilmember Alex Pedersen", "Seattle", "alex.pedersen@seattle.gov"),
            ( "Councilmember Debora Juerez", "Seattle", "debora.juarez@seattle.gov"),
            ( "Councilmember Dan Strauss", "Seattle", "dan.strauss@seattle.gov"),
            ( "Councilmember Andrew Lewis", "Seattle", "andrew.lewis@seattle.gov"),
            ( "Councilmember Teresa Mosqueda", "Seattle", "teresa.mosqueda@seattle.gov"),
        ],
    },
}

def get_all():
    recv = []
    for state in mailing_list:
        for county in mailing_list[state]:
            recv.extend(mailing_list[state][county])
    return recv

def get_state(state):
    recv = []
    for county in mailing_list[state]:
        recv.extend(mailing_list[state][county])
    return recv

def get_city(state, county):
    return mailing_list[state][county]

def get_states():
    lst = ["Select All"]
    lst.extend(mailing_list.keys())
    return lst

def get_cities(state):
    lst = ["Select All"]
    lst.extend(mailing_list[state].keys())
    return lst
