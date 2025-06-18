<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    </head>
    <style>
        .over {
            background-color: orange;
        }
        .selected {
            background-color: green;
        }
    </style>

    <body>
        <div id="buttons"></div>
        <table id= "potter" border='1'>
            <thead class="tHead"><tr>
                <th>name</th>
                <th>role</th>
                <th>house</th>
                <th>gender</th>
                <th>alignment</th>
            </tr></thead>
            <tbody></tbody>
        </table>
        <button id="reset">reset</button>
        <button id="Gryffindor">Gryffindor</button>
        <button id="Hufflepuff">Hufflepuff</button>
        <button id="Slytherin">Slytherin</button>
        <button id="Ravenclaw">Ravenclaw</button>
    </body>

        <script>
        //$(function() {
        //data about characters goes here
        // list of characters

        var characters = [
        {name:"Albus Dumbledore", role:"staff", house:"Gryffindor",gender:"m",alignment:"good"},    
        {name:"Nymphadora Tonks", role:"", house:"Hufflepuff",gender:"f",alignment:"good"},    
        {name:"Ron Weasley", role:"student", house:"Gryffindor",gender:"m",alignment:"good"},    
        {name:"Ginny Weasley", role:"student", house:"Gryffindor",gender:"f",alignment:"good"},    
        {name:"Hermione Granger", role:"student", house:"Gryffindor",gender:"f",alignment:"good"},    
        {name:"Mad-eye Moody", role:"staff", house:"",gender:"m",alignment:"good"},    
        {name:"Prof McGonagall", role:"staff", house:"Gryffindor",gender:"f",alignment:"good"},    
        {name:"Harry Potter", role:"student", house:"Gryffindor",gender:"m",alignment:"good"},    
        {name:"Draco Malfoy", role:"student", house:"Slytherin",gender:"m",alignment:"evil"},    
        {name:"Hagrid", role:"staff", house:"Gryffindor",gender:"m",alignment:"good"},    
        {name:"Luna Lovegood", role:"student", house:"Ravenclaw",gender:"f",alignment:"good"},    
        {name:"Voldemort", role:"", house:"Slytherin",gender:"m",alignment:"evil"},    
        {name:"Bellatrix Lestrange", role:"", house:"Slytherin",gender:"f",alignment:"evil"},           
        {name:"Severus Snape", role:"staff", house:"Slytherin",gender:"m",alignment:"?"}
        ];
            
        
        $(document).ready(function(){
            $('button').click(function() {
                let house = $(this).text();
                $("tr:not(:first)").hide();
                $('tr').filter((i, row) => {
                    console.log(row.children[2].innerText);
                    return row.children[2].innerText == house;
                }).show();
                
                if($(this).attr('id') == 'reset'){
                    $('tr').show()
                };
              
                
                /*$("button:contains('reset')").document.getElementById('potter');*/
                //document.querySelector("table").show();
        });
            $("tr:even").css("background-color", "yellow");
            $("tr:odd").css("background-color", "orange");
            $("th").css("background-color", "lightgrey");
  });
            //function acts as a filter
        function Characters(characters)
        {
        //declare characters()
            return (characters.name)&&(characters.role)&&(characters.house)&&(characters.gender);
           
        }
      

        //Filtering code goes here - creates a new array called results
        // CHECKS EACH PERSON AND ADDS THOSE IN RANGE TO ARRAY
        var results = [];
        characters.forEach(function(characters){
            if(characters.name&&characters.role&&characters.house&&characters.gender&&characters.alignment){
                results.push(characters);
            }
        })
        
        /*filer the characters array & add matches to the results array
        var results = [];
        //array for matching characters
        results = characters.filter(Characters);
        //filter calls Characters*/

        //loop through new array and add matching characters to the results table
        var $tableBody = $('<tbody></tbody>');//new table body jquery 
        for (var i = 0; i < characters.length; i++){//loop through matches
            //var newCharacters = characters[i];//store current characters
            var $row = $('<tr></tr>');//create new row for characters
            $row.append($('<td></td>').text(characters[i].name));//add their name
            $row.append($('<td></td>').text(characters[i].role));//add their role
            $row.append($('<td></td>').text(characters[i].house));//add their house
            $row.append($('<td></td>').text(characters[i].gender));//add their gender
            $row.append($('<td></td>').text(characters[i].alignment));//add their alignment
            $tableBody.append( $row );// Add row to new content

            console.log(characters[i].house);
        }
        
        $('thead').after($tableBody);// Add tbody after thead
        
        /*
        - add a button for each 'house' value
        - add table row for each character
        - set visible rows to alternating background color
            
        - add click handler to show only rows matching selected 'house'. Enable buttons to call this handler. 
        
        - add click handler to reset table 
        */

        //});

        </script>
</html>
