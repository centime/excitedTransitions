path="./tables/"
SS="$1h$2p$3"

echo $SS


python2 ./gen.py $1 $2 $3

python2 ./writeTransition.py out

python2 ./sort_clean.py out_tran

mv cleaned "$path$SS"
echo "Saved in $path$SS"
