<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:wix="http://wixtoolset.org/schemas/v4/wxs"
    exclude-result-prefixes="wix">

    <xsl:output method="xml" indent="yes" omit-xml-declaration="yes" />

    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="wix:File[@KeyPath='yes']">
        <xsl:copy>
            <xsl:apply-templates select="@*[local-name() != 'KeyPath']" />
        </xsl:copy>
        
        <xsl:element name="RegistryValue" namespace="http://wixtoolset.org/schemas/v4/wxs">
            <xsl:attribute name="Root">HKCU</xsl:attribute>
            <xsl:attribute name="Key">Software\Grishka\H20\Files</xsl:attribute>
            <xsl:attribute name="Name"><xsl:value-of select="@Id"/></xsl:attribute>
            <xsl:attribute name="Type">string</xsl:attribute>
            <xsl:attribute name="Value">1</xsl:attribute>
            <xsl:attribute name="KeyPath">yes</xsl:attribute>
        </xsl:element>
    </xsl:template>
</xsl:stylesheet>