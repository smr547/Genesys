# Flask App patterns

## Endpoints
The [Contacts App](https://github.com/bigskysoftware/contact-app/tree/master) defines the following endpoints

<table>
  <tr>
    <th>Route</th>
    <th>Method</th>
    <th>Server action</th>
  </tr>
  <tr>
<tr>
<td>/</td>
  <td>GET</td>
  <td>Redirect to /contents</td>
</tr>
<tr>
  <td>/contacts</td>
  <td>GET</td>
  <td></td>
</tr>
  <tr>
  <td>/contacts/archive</td>
  <td>POST</td>
  <td></td>
</tr>
  <tr>
  <td>/contacts/archive</td>
  <td>GET</td>
  <td></td>
</tr>
  <tr>
  <td>/contacts/archive/file</td>
  <td>GET</td>
  <td></td>
</tr>
  <tr>
  <td>/contacts/archive</td>
  <td>DELETE</td>
  <td></td>
</tr>
<tr>
  <td>/contacts/count</td>
  <td>GET</td>
  <td>Returns a count of the number of Contacts</td>
</tr>
<tr>
  <td>/contacts/new</td>
  <td>GET</td>
  <td>Return a form to allow new contact details to be entered</td>
</tr>
  <tr>
  <td>/contacts/new</td>
  <td>POST</td>
  <td>Create a new contact form the supplied form data or return error(s)</td>
</tr>
<tr>
  <td>/contacts/&lt;contact_id&gt;</td>
  <td>GET</td>
  <td>Return display data for specified ``contact_id``</td>
</tr>
<tr>
  <td>/contacts/&lt;contact_id&gt;/edit</td>
  <td>GET</td>
  <td>Return form to allow editing of data for specified ``contact_id``</td>
</tr>
<tr>
  <td>/contacts/&lt;contact_id&gt;/edit</td>
  <td>POST</td>
  <td>Update data for specified ``contact_id``</td>
</tr>
<tr>
  <td>/contacts/&lt;contact_id&gt;</td>
  <td>DELETE</td>
  <td>Delete specified contact</td>
</tr>
  <td>/contacts</td>
  <td>DELETE</td>
  <td>Delete selected Contacts</td>
</tr>
<tr>
  <td>/api/v1/contacts</td>
  <td>GET</td>
  <td>Return all Contacts as a JSON array</td>
</tr>
<tr>
  <td>/api/v1/contacts</td>
  <td>POST</td>
  <td>Create a new contact</td>
</tr>
<tr>
  <td>/api/v1/contacts/&lt;contact_id&gt;</td>
  <td>GET</td>
  <td>Return a JSON representation of the specified Contact</td>
</tr>
<tr>
  <td>/api/v1/contacts/&lt;contact_id&gt;</td>
  <td>PUT</td>
  <td>Amend the specified Contact</td>
</tr>
<tr>
  <td>/api/v1/contacts/&lt;contact_id&gt;</td>
  <td>DELETE</td>
  <td>Delete the specified Contact</td>
</tr>
</table>
