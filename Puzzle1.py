input = """
    329419947132719599482483219756485987668263818888976829889424383266565468
    141288686223452599155327657864126558995917841421838932936149667399161467
    362634455217941399556226681813837239321396614312491446939769258725111266
    321786287923322676353391112889335453635321384712225146385789415981982872
    482796957643219184778777273288126687546972118933188222814657683292131463
    822131739325647199859811728963268466335527384598393384572171349781176699
    536779585796522218366876551745426335411113484133463134511159613168272619
    657476316518788933759958334563441343616553974418886615677158564771855518
    252993666968358166239861876539148716471572484989456331442695934811928695
    514443945273176266656874161215325446913172413769983298472893786595671192
    559262845661713369525955454871932822993862133232512597254718123681226388
    737586623111831295436943293735935726646738331832623957287731476512184483
    112617817398879976521891317882596626881647655979294735995685998922891713
    626717857177631634529257348987379214964654874799538966969218845772441446
    872719281991944827592216632115814136523754522263368837289145184243445852
    769877434211148249899938383149257761515459127871965679827737736328437946
    875799837319323179576764465415543269298865131284543351187945792163893487
    755757524139436372166723777896245596149355984852258241374821897121248637
    323279587836296487385599469714969282491718337554519211945358739819991256
    447461421992934518546866112996637969381349854247473219817649669474611157
    692571549396729648725823785415238236557987689439181575981537331915921347
    555525148875427988824549237359547118919135324468469766284837652988151252
    922162731352744122145967278692314516598961122337224114992943624737481846
    748164193187297258229542593699853519442391654436779952227691444523158227
    236838883183443756275211932528647435286355469337371884864956845179775192
    631561757529538196442684362528281952474711972687219356978561195989677614
    353991529996827637471299648536785349473437625751127344373643346449628721
    9615697341973131715166768916149828396454638596713572963686159214116763
    """


input = input.replace("\n", "")
input = input.replace(" ", "")
print(input)
total = 0

print(len(input))

for i in range(len(input) -1):
  if input[i] == input[i+1]:
    print(input[i])
    total += int(input[i])

if input[-1] == input[0]:
  total += int(input[-1])

print(total)
