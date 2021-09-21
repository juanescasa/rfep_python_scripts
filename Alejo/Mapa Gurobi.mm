<map version="freeplane 1.9.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Gurobi" FOLDED="false" ID="ID_696401721" CREATED="1610381621824" MODIFIED="1631488039861" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle" zoom="1.61">
    <properties fit_to_viewport="false" edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ID="ID_271890427" ICON_SIZE="12 pt" COLOR="#000000" STYLE="fork">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_271890427" STARTARROW="DEFAULT" ENDARROW="NONE"/>
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
<richcontent CONTENT-TYPE="plain/auto" TYPE="DETAILS"/>
<richcontent TYPE="NOTE" CONTENT-TYPE="plain/auto"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.selection" BACKGROUND_COLOR="#4e85f8" STYLE="bubble" BORDER_COLOR_LIKE_EDGE="false" BORDER_COLOR="#4e85f8"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important" ID="ID_67550811">
<icon BUILTIN="yes"/>
<arrowlink COLOR="#003399" TRANSPARENCY="255" DESTINATION="ID_67550811"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10 pt" SHAPE_VERTICAL_MARGIN="10 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="24" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/RevisionPlugin.properties"/>
<node TEXT="Introduction: Mathematical Optimization Models" FOLDED="true" POSITION="right" ID="ID_1348379384" CREATED="1631486370397" MODIFIED="1631487074707" BACKGROUND_COLOR="#ffffff" HGAP_QUANTITY="12.5 pt" VSHIFT_QUANTITY="-48.75 pt">
<edge COLOR="#0000ff"/>
<node TEXT="Should be solvable in a reasonable amount of time  (efficient)" ID="ID_1629464341" CREATED="1631486441078" MODIFIED="1631487067791" VSHIFT_QUANTITY="-18.75 pt" BACKGROUND_COLOR="#ffffff"/>
<node TEXT="Capture the key features of the problem (effective)" ID="ID_1539608162" CREATED="1631486443805" MODIFIED="1631487074706" BACKGROUND_COLOR="#ffffff" HGAP_QUANTITY="18.5 pt" VSHIFT_QUANTITY="20.25 pt"/>
</node>
<node TEXT="Mathematical Programming" FOLDED="true" POSITION="right" ID="ID_1594505146" CREATED="1631486708110" MODIFIED="1631487078739" BACKGROUND_COLOR="#ffffff" HGAP_QUANTITY="35 pt" VSHIFT_QUANTITY="-46.5 pt">
<edge COLOR="#7c007c"/>
<node TEXT="Declaritve approach where the modeler formulates&#xa;a mathematical optimization problem" ID="ID_558227388" CREATED="1631486724208" MODIFIED="1631487085858" BACKGROUND_COLOR="#ffffff">
<node TEXT="Captures the key features of a complex decision problem" ID="ID_717471197" CREATED="1631486872750" MODIFIED="1631487085857" BACKGROUND_COLOR="#ffffff" HGAP_QUANTITY="14.75 pt" VSHIFT_QUANTITY="-2.25 pt"/>
</node>
<node TEXT="Formulations can be solved by Linear Programming or Mixed Integer Programming" ID="ID_473748198" CREATED="1631486913182" MODIFIED="1631487059886" BACKGROUND_COLOR="#ffffff"/>
<node TEXT="We dont have to worry about how to solve the problem" ID="ID_829438528" CREATED="1631487121026" MODIFIED="1631487165513" BACKGROUND_COLOR="#ffff00"/>
</node>
<node TEXT="Linear Programming" FOLDED="true" POSITION="right" ID="ID_1765484358" CREATED="1631487619351" MODIFIED="1631488129734" BACKGROUND_COLOR="#ffffff" HGAP_QUANTITY="23.75 pt" VSHIFT_QUANTITY="-16.5 pt">
<edge COLOR="#ff0000"/>
<node TEXT="A problem that seeks to optimize the revenue of&#xa; a companie based on:" ID="ID_457151859" CREATED="1631487642839" MODIFIED="1631488129733" BACKGROUND_COLOR="#ffffff">
<node TEXT="Products" ID="ID_179014416" CREATED="1631487902680" MODIFIED="1631488065295" BACKGROUND_COLOR="#ffffff">
<node TEXT="Tables" ID="ID_1966326720" CREATED="1631487980202" MODIFIED="1631488072855" BACKGROUND_COLOR="#ffffff"/>
<node TEXT="Chairs" ID="ID_427419561" CREATED="1631487985688" MODIFIED="1631488077451" BACKGROUND_COLOR="#ffffff"/>
</node>
<node TEXT="Resources" ID="ID_674818870" CREATED="1631487942264" MODIFIED="1631488082120" BACKGROUND_COLOR="#ffffff">
<node TEXT="Mahogany" ID="ID_1627210793" CREATED="1631487992767" MODIFIED="1631488087884" BACKGROUND_COLOR="#ffffff"/>
<node TEXT="Labor" ID="ID_375886977" CREATED="1631487998585" MODIFIED="1631488091595" BACKGROUND_COLOR="#ffffff"/>
</node>
<node TEXT="Constrains of capacity" ID="ID_591031280" CREATED="1631488005936" MODIFIED="1631488097148" BACKGROUND_COLOR="#ffffff" VSHIFT_QUANTITY="6.75 pt"/>
</node>
</node>
<node TEXT="Modeling and Solving Linear Programming Problems" FOLDED="true" POSITION="right" ID="ID_739220869" CREATED="1631488156058" MODIFIED="1631488298975" BACKGROUND_COLOR="#ffffff">
<edge COLOR="#0000ff"/>
<node TEXT="Made with Python and gurobipy (see notebook)" ID="ID_1615194762" CREATED="1631488191599" MODIFIED="1631488304737" BACKGROUND_COLOR="#ffffff">
<node TEXT="Can be solved:" ID="ID_1940442742" CREATED="1631488230632" MODIFIED="1631488309415" BACKGROUND_COLOR="#ffffff">
<node TEXT="Manually var by var and constr by constr" ID="ID_223606641" CREATED="1631488240320" MODIFIED="1631488317538" BACKGROUND_COLOR="#ffffff"/>
<node TEXT="Parametrized with multidicts" ID="ID_1310389202" CREATED="1631488263179" MODIFIED="1631488322481" BACKGROUND_COLOR="#ffffff"/>
</node>
</node>
</node>
</node>
</map>
