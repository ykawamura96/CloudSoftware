items=(newplot.png
       newplot1.png
       newplot11.png
       newplot13.png
       newplot15.png
       newplot2.png
       newplot5.png
       newplot7.png
       newplot9.png
       result.png
       newplot04.png
       newplot10.png
       newplot12.png
       newplot14.png
       newplot16.png
       newplot3.png
       newplot6.png
       newplot8.png)
for item in "${items[@]}" ; do
    a=`echo $item | sed -e "s/png/pdf/g"`
    convert $item $a
done
