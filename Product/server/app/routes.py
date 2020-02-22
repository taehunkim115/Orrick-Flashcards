from app import app
import lexnlp.nlp.en.segments.sentences as lex_sentences
import lexnlp.extract.en.dates as lex_dates

@app.route('/')
@app.route('/index')
def index():
    sample = '''
STATEMENT OF ISSUES 
1. As the Board recognized, the most important bargaining issue between DISH and the union was QPC. DISH was clear that it would not agree to retain QPC in any form. Following lengthy and unsuccessful negotiations, the union insisted on keeping QPC. DISH made and then implemented its last, best, and final offer. 
Was the Board’s determination that DISH improperly implemented its last, best, and final offer in the absence of a valid impasse supported by substantial evidence, where it was based entirely on the ALJ’s incorrect conclusion that there was a high attrition rate among DISH technicians at the two unionized Dallas locations? 
2. After DISH implemented its last, best, and final offer, 17 employees quit. The evidence is undisputed, and all parties and the ALJ agreed, that these employees quit because their wages were reduced. This Court and the Board have held that a unilateral wage reduction, standing alone, does not create a Hobson’s Choice such that employees who quit because of the reduction were necessarily constructively discharged. Did the Board err in nonetheless concluding 
6 
Case: 18-60522 Document: 00514736148 Page: 17 Date Filed: 11/26/2018 
that these employees were constructively discharged because they faced a Hobson’s Choice? 
STATEMENT OF THE CASE 
DISH Tries QPC On A Trial Basis; Technicians Oppose It And Unionize To Eliminate It 
DISH is one of the largest providers of TV programming in the country. It sells programming packages to its customers, which it beams via satellite to small dishes mounted on their homes. To provide this service, DISH employs technicians who travel to customers’ homes to install the satellite systems and troubleshoot any problems. ROA.876. DISH generally compensates its technicians using a nationwide pay system, ROA.1076, which often included an hourly component. In 2009, DISH began a pilot program to test QPC, a new incentive-based system at several locations, including two of its eight offices in the North Texas region: Farmers Branch and North Richland Hills. ROA.882-83. 
The idea behind this system was to supplement a lower hourly wage with additional, performance-based compensation. ROA.881. Each task a technician might perform was assigned a point value. These points were then weighted (based on how well the technician 
7 
Case: 18-60522 Document: 00514736148 Page: 18 Date Filed: 11/26/2018 
performed the task) and assigned dollar values. Id. Technicians thus accrued both hourly wages and incentive pay throughout the day, and their pay increased with the quantity and quality of tasks they performed. The goal of QPC was to develop a merit-based compensation system that would “drive performance” while “not increas[ing] pay to a drastic point.” Id. 
The technicians in Farmers Branch and North Richland Hills fervently opposed QPC because it decreased their hourly base wage. ROA.1076-77 (Basara deposition testimony); ROA.2171 (ALJ order). They wanted to eliminate QPC and return to a system of flat hourly wages—so much so that they began a union drive that led to the election of the Communications Workers of America (“the Union”) to represent them in collective bargaining. ROA.1076. 
With the Union in place, collective bargaining was required for wages and other mandatory subjects of bargaining. 29 U.S.C. § 158(d). The Union initially sought a contract that would eliminate QPC at the Dallas-area locations and move back to the system of higher, flat hourly wages that had existed before; after all, opposition to QPC was the very impetus for unionization. ROA.1081-82. For its part, DISH originally 
8 
Case: 18-60522 Document: 00514736148 Page: 19 Date Filed: 11/26/2018 
wanted to preserve QPC. Id. But DISH quickly abandoned that position when it replaced the QPC pilot program elsewhere in the country with a different performance-based incentive program, Pi. ROA.1083, 2172 (ALJ).1 
Collective bargaining between DISH and the Union began in July 2010, ROA.2168, and during the first years of bargaining, the parties met approximately a dozen times, for a total of 20 to 25 days. ROA.1086 (Basara); ROA.2172 (ALJ). By early 2013, substantial progress had been made. Both sides agreed that QPC should be replaced with a system of hourly wages, plus the opportunity to earn additional pay under Pi.2 The only remaining wage-based issues 
1 Pi pays a higher hourly wage and is less heavily incentive-based than QPC. ROA.1076-77. And whereas everyone under QPC earned some incentive-based pay, a technician paid under Pi had to meet certain thresholds before earning incentive-based pay. In addition, incentives under Pi were capped for each pay period, whereas QPC had no limit on the additional wages an employee could receive. ROA.881, 883-85. In short, under Pi, all technicians earn a greater hourly wage compared to QPC, and technicians who “perform above and beyond” are “rewarded with a little extra.” ROA.883. 
2 ROA.1083-84, 1089-93; ROA.1410 (Union’s March 22, 2013 proposal, indicating that “[a]ll bargaining unit employees will participate in the same incentive programs as other non-represented DISH network 
    '''

    processed_brief = lex_sentences.pre_process_document(sample)
    sentences_brief = lex_sentences.get_sentence_list(processed_brief)

    facts = []
    for sentence in sentences_brief:
        dates = lex_dates.get_dates(sentence)
    for date in dates:
        facts.append((date,sentence))

    r = ''

    for fact in facts:
        r += "Question:\nWhy is {} significant?\n\nAnswer:\n{}".format(str(fact[0]), fact[1])
        r += '\n'

    return r