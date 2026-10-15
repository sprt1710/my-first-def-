



factor=[]
from abgoosht import*
import abgoosht
from doogh import*
import doogh

while True:

    meno=input("1.ghaza  2.nooshidani 3.exit: ")
    while True:
        match meno:
            case "1":
                meno_ghaza=input("1.abgoosht 2.exit: ")
                tedad_abgoosht=int(input("chanta mikhay? :"))
                mablagh_abgoosht=int(("input(cheghdr shode? :"))
                abgoosht(mablagh_abgoosht,tedad_abgoosht)
                break

            case "2":
                meno_nooshidani=input("1.doogh 2.exit :")
                tedad_nooshidani=int(input("chanta mikhay? :"))
                mablagh_nooshidani=int(input("cheghadr shode? :"))
                doogh(mablagh_nooshidani,tedad_nooshidani)
                break

            case "3":
                break

