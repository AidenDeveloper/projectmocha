import sqlite3


from RNGFailSystem import (sucNum, failNum, failTaste, failSpill, failLook, failTemp)

data = sqlite3.connect('analytics.db')

i = data.cursor()


#i.execute("""CREATE TABLE analytics (
#            save text,
#            suc integer,
#            fail integer,
#            taste integer,
#            look integer,
#            spill integer,
#            temp integer
#            )""")

#i.execute("INSERT INTO analytics VALUES ('saveEntry', 0, 0, 0, 0, 0, 0)")


data.commit()

i.execute("SELECT suc FROM analytics WHERE save='saveEntry'")
xsucNumTot = (i.fetchone())

i.execute("SELECT fail FROM analytics WHERE save='saveEntry'")
xfailNumTot = (i.fetchone())

i.execute("SELECT taste FROM analytics WHERE save='saveEntry'")
xfailTasteTot = (i.fetchone())

i.execute("SELECT look FROM analytics WHERE save='saveEntry'")
xfailLookTot = (i.fetchone())

i.execute("SELECT spill FROM analytics WHERE save='saveEntry'")
xfailSpillTot = (i.fetchone())

i.execute("SELECT temp FROM analytics WHERE save='saveEntry'")
xfailTempTot = (i.fetchone())

data.commit()


sucNumTot = xsucNumTot[0] + sucNum
failNumTot = xfailNumTot[0] + failNum
failTasteTot = xfailTasteTot[0] + failTaste
failLookTot = xfailLookTot[0] + failLook
failSpillTot = xfailSpillTot[0] + failSpill
failTempTot = xfailTempTot[0] + failTemp


print()
print("attempts = ", (sucNumTot + failNumTot))
print("fails = ", failNumTot)
print("successes = ", sucNumTot)
print("fail rate = ", float(int(float(failNumTot / (sucNumTot + failNumTot)) * 100000) / 1000), "%")

print("\nfails:")
if failNumTot > 0:
    print("taste: ", float(int(float((failTasteTot / failNumTot) * 100000)) / 1000), "%")
    print("look: ", float(int(float((failLookTot / failNumTot) * 100000)) / 1000), "%")
    print("spill: ", float(int(float((failSpillTot / failNumTot) * 100000)) / 1000), "%")
    print("temp.", float(int(float((failTempTot / failNumTot) * 100000)) / 1000), "%")

else:
    print("NO FAILS!")


def update_suc(suc):
    with data:
        i.execute("""UPDATE analytics SET suc = :suc WHERE save = 'saveEntry'""", {'suc': sucNumTot})

def update_fail(fail):
    with data:
        i.execute("""UPDATE analytics SET fail = :fail WHERE save = 'saveEntry'""", {'fail': failNumTot})

def update_taste(taste):
    with data:
        i.execute("""UPDATE analytics SET taste = :taste WHERE save = 'saveEntry'""", {'taste': failTasteTot})

def update_look(look):
    with data:
        i.execute("""UPDATE analytics SET look = :look WHERE save = 'saveEntry'""", {'look': failLookTot})

def update_spill(spill):
    with data:
        i.execute("""UPDATE analytics SET spill = :spill WHERE save = 'saveEntry'""", {'spill': failSpillTot})

def update_temp(temp):
    with data:
        i.execute("""UPDATE analytics SET temp = :temp WHERE save = 'saveEntry'""", {'temp': failTempTot})

update_suc(sucNumTot)
update_fail(failNumTot)
update_taste(failTasteTot)
update_look(failLookTot)
update_spill(failSpillTot)
update_temp(failTempTot)

i.execute("SELECT * FROM analytics WHERE save='saveEntry'")
print(i.fetchone())
print(sucNumTot)

data.commit()

data.close()